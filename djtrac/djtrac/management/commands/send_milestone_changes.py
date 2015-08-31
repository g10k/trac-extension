# encoding: utf8
import re
from copy import deepcopy
import lxml.html
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from djtrac import models
from djtrac.datatools.users import get_user_tickets


def _save_user_tickets(user, left_tickets, new_tickets):
    if type(user) in (str, unicode):
        user = User.objects.get(username=user)

    models.UserCurrentMilestoneTicket.objects.filter(user=user, ticket__in=left_tickets).delete()

    for ticket_id in new_tickets:
        models.UserCurrentMilestoneTicket.objects.create(user=user, ticket=ticket_id)

    # TODO: добавить сохранении в models.UserNotification

def get_ticket_changes():
    ticket_changes = {}
    default_milestone_info = {'new': set(), 'left': set()}
    for user in User.objects.filter(user_projects__send_milestone_changes=True):
        user_milestones = ticket_changes.setdefault(user.username, {})

        actual_user_tickets = set(get_user_tickets(user, only_milestone_changes=True))
        last_notified_tickets = set(user.last_notified_tickets.values_list('ticket', flat=True))
        new_tickets = actual_user_tickets - last_notified_tickets
        left_tickets = last_notified_tickets - actual_user_tickets

        for new_ticket_id in new_tickets:
            ticket = models.Ticket.objects.get(id=new_ticket_id)
            user_milestone = user_milestones.setdefault(ticket.milestone, deepcopy(default_milestone_info))
            user_milestone['new'].add(ticket)

        for left_ticket_id in left_tickets:
            ticket = models.Ticket.objects.get(id=left_ticket_id)
            user_milestone = user_milestones.setdefault(ticket.milestone, deepcopy(default_milestone_info))
            user_milestone['left'].add(ticket)

    return ticket_changes


class Command(BaseCommand):
    args = ''
    help = u'Щлет уведомления об изменениях по тикетам текущих этапов пользователей, ' \
           u'подписанных на изменения.'

    def handle(self, *args, **options):
        # TODO: добавить бесконечный цикл

        ticket_changes = get_ticket_changes()
        for user, milestones_tickets in ticket_changes.iteritems():
            if not milestones_tickets:
                continue

            html_content = render_to_string(
                'djtrac/mail/ticket_changes.html',
                {'milestones_tickets': milestones_tickets}
            )

            subject = u'Изменения по "%s"' % u'", "'.join(milestones_tickets.keys())
            user_instance = User.objects.get(username=user)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user_instance.email]

            text_content = lxml.html.fromstring(html_content).text_content()
            text_content = re.sub(r'\n\s+', '\n', text_content).strip()

            sent_count = send_mail(
                subject,
                text_content,
                html_message=html_content,
                from_email=from_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )

            if sent_count:
                new_tickets = []
                left_tickets = []
                for milestone_tickets in milestones_tickets.values():
                    new_tickets.extend(milestone_tickets['new'])
                    left_tickets.extend(milestone_tickets['left'])

                _save_user_tickets(
                    user,
                    new_tickets=[t.id for t in new_tickets],
                    left_tickets=[t.id for t in left_tickets],
                )



