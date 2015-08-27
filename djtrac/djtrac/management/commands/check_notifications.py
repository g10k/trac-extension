# encoding: utf8

'''
    Команда для ежедневной рассылки
'''
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from djtrac.models.trac_models import Ticket
from django.contrib.auth.models import User
from djtrac.models import trac_models


def get_tickets():
    #
    # ['user']['project'] = {'changed_tickets': {2:message, 3:message}, 'new_tickets': [5, 6, 7],'current_milestone':u"МИС ММ 2015-07."}
    #
    res = {}
    for user in User.objects.filter(user_projects__notification__isnull=False):
        res[user.username] = {}
        for up in user.user_projects.filter(notification__isnull=False):

            current_milestones = list(up.project.allowed_milestones.filter(is_current=True).values_list('milestone_name', flat=True))
            # Подразумевается, что current_milestone один.
            current_milestone = current_milestones[0] if current_milestones else None
            if not current_milestone:
                continue
            project_tickets_current = list(Ticket.objects.filter(milestone=current_milestone).values_list('id', flat=True))
            already_notificated_tickets_history = user.notification_history.filter(notificated_milestone=current_milestone)
            # Если тикет больше не в проекте, то тут такие всплывут.
            changed_tickets = set(already_notificated_tickets_history.values_list('ticket', flat=True)) - set(project_tickets_current)
            changed_tickets = {ticket: u"Теперь больше не относится к проекту" for ticket in changed_tickets }

            # Проходим по всем тикетам, по которым уже были высланы уведомления и проверяем в прежнем ли они состоянии.
            for ticket_notification in already_notificated_tickets_history:
                actual_ticket = trac_models.Ticket.objects.get(id=ticket_notification.ticket)
                if ticket_notification.notificated_milestone != actual_ticket.milestone:
                    changed_tickets[ticket_notification.ticket] = u"Изменил этап с %s на %s" % (ticket_notification.notificated_milestone, actual_ticket.summary)
            res[user.username][up.project.name] = {
                'changed_tickets': changed_tickets,
                'new_tickets': set(project_tickets_current) - set(already_notificated_tickets_history.values_list('ticket', flat=True)),
                'current_milestone': current_milestone
            }
    return res

class Command(BaseCommand):
    args = ''
    help = u'проверяем по всем ли тикетам были высланы уведомления, возвращаем те, по которым не высланы.'


    def handle(self, *args, **options):
        tickets_for_mailing = get_tickets()
        for user, projects in tickets_for_mailing.items():

            email_text = u'Уведомление soft-way.\r\n'
            email_text += u'Произошли изменения в проектах %s' % ', '.join(projects.keys())
            for project, project_tickets in projects.items():
                html_message = render_to_string('djtrac/mail.html', {'project':project, 'project_tickets': project_tickets})
                send_mail('Subject here', html_message, 'from@example.com', ['g10k.info@gmail.com'], fail_silently=False, html_message=html_message)

