# encoding: utf8

'''
    Команда для ежедневной рассылки
'''
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from djtrac.models.extra_models import UserCurrentMilestoneTicket
from djtrac.datatools.users import get_user_tickets

NEW_TICKETS = 'new_tickets'
LEFT_TICKETS = 'left_tickets'


def _save_user_tickets(user, left_tickets, new_tickets):
    if type(user) in (str, unicode):
        user = User.objects.get(username=user)
    UserCurrentMilestoneTicket.objects.filter(user=user, ticket__in=left_tickets).delete()
    for ticket_id in new_tickets:
        UserCurrentMilestoneTicket.objects.create(user=user, ticket=ticket_id)


def get_mailing_info():
    mailing_info = {}
    for user in User.objects.filter(user_projects__notification=True):
        if user.username not in mailing_info:
            mailing_info[user.username] = {NEW_TICKETS: set(), LEFT_TICKETS: set()}
        all_user_tickets = get_user_tickets(user, only_notification=True)
        last_notified_tickets = list(user.last_notified_tickets.values_list('ticket', flat=True))
        new_tickets = set(all_user_tickets) - set(last_notified_tickets)
        left_tickets = set(last_notified_tickets) - set(all_user_tickets)
        mailing_info[user.username][NEW_TICKETS].update(new_tickets)
        mailing_info[user.username][LEFT_TICKETS].update(left_tickets)
    return mailing_info


class Command(BaseCommand):
    args = ''
    help = u'проверяем по всем ли тикетам были высланы уведомления, возвращаем те, по которым не высланы.'

    def handle(self, *args, **options):

        mailing_info = get_mailing_info()
        for user, all_tickets in mailing_info.iteritems():
            html_message = render_to_string('djtrac/simple_email.html', {'all_tickets': all_tickets})
            user_instance = User.objects.get(username=user)
            sended = send_mail(
                'Оповещение trac extension',
                html_message,
                settings.EMAIL_HOST_USER,
                [user_instance.email],
                fail_silently=False,
                html_message=html_message
            )
            if sended:
                _save_user_tickets(user, all_tickets.get(LEFT_TICKETS), all_tickets.get(NEW_TICKETS))



