# encoding: utf8

'''
    Команда для ежедневной рассылки
'''
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.db.models import Q
from django.template.loader import render_to_string
from djtrac.models.trac_models import Ticket
from djtrac.models.extra_models import Notification, UserTicketNotification

from django.contrib.auth.models import User
from djtrac.models import trac_models


#
# def get_tickets():
#     #
#     # ['user']['project'] = {'changed_tickets': {2:message, 3:message}, 'new_tickets': [5, 6, 7],'current_milestone':u"МИС ММ 2015-07."}
#     #
#     res = {}
#     for user in User.objects.filter(user_projects__notification__isnull=False):
#         res[user.username] = {}
#         for up in user.user_projects.filter(notification__isnull=False):
#
#             current_milestones = list(up.project.allowed_milestones.filter(is_current=True).values_list('milestone_name', flat=True))
#             # Подразумевается, что current_milestone один.
#             current_milestone = current_milestones[0] if current_milestones else None
#             if not current_milestone:
#                 continue
#             project_tickets_current = list(Ticket.objects.filter(milestone=current_milestone).values_list('id', flat=True))
#             already_notificated_tickets_history = user.notification_history.filter(notificated_milestone=current_milestone)
#             # Если тикет больше не в проекте, то тут такие всплывут.
#             changed_tickets = set(already_notificated_tickets_history.values_list('ticket', flat=True)) - set(project_tickets_current)
#             changed_tickets = {ticket: u"Теперь больше не относится к проекту" for ticket in changed_tickets }
#
#             # Проходим по всем тикетам, по которым уже были высланы уведомления и проверяем в прежнем ли они состоянии.
#             for ticket_notification in already_notificated_tickets_history:
#                 actual_ticket = trac_models.Ticket.objects.get(id=ticket_notification.ticket)
#                 if ticket_notification.notificated_milestone != actual_ticket.milestone:
#                     changed_tickets[ticket_notification.ticket] = u"Изменил этап с %s на %s" % (ticket_notification.notificated_milestone, actual_ticket.summary)
#             res[user.username][up.project.name] = {
#                 'changed_tickets': changed_tickets,
#                 'new_tickets': set(project_tickets_current) - set(already_notificated_tickets_history.values_list('ticket', flat=True)),
#                 'current_milestone': current_milestone
#             }
#     return res

def get_user_tickets(user):
    tickets = []
    for up in user.user_projects.filter(notification=True):
        current_milestones = list(up.project.allowed_milestones.filter(is_current=True).values_list('milestone_name', flat=True))
        tickets.extend(list(Ticket.objects.filter(milestone__in=current_milestones).values_list('id', flat=True)))
    return tickets

def save_user_tickets(user, left_tickets, new_tickets):
    if type(user) in (str, unicode):
        user = User.objects.get(username=user)
    UserTicketNotification.objects.filter(user=user, ticket__in=left_tickets).delete()
    for ticket_id in new_tickets:
        UserTicketNotification.objects.create(user=user, ticket=ticket_id)


def get_mailing_info():
    mailing_info = {}
    # mailing_info.setdefault({'new_tickets': [],'left_tickets':[]})
    for user in User.objects.filter(user_projects__notification=True):
        # for up in user.user_projects.filter(notification=True):
        if user.username not in mailing_info:
            mailing_info[user.username] = {'new_tickets': set(),'left_tickets':set()}
        all_user_tickets = get_user_tickets(user)
        last_notified_tickets = list(user.last_notified_tickets.values_list('ticket', flat=True))
        new_tickets = set(all_user_tickets) - set(last_notified_tickets)
        left_tickets = set(last_notified_tickets) - set(all_user_tickets)
        # if user.username in mailing_info and 'new_tickets' in mailing_info[user.username]:
        mailing_info[user.username]['new_tickets'].update(new_tickets)
        mailing_info[user.username]['left_tickets'].update(left_tickets)
    return mailing_info

def not_notificated():
    # TODO: Переименовать res
    res = {}
    for user in User.objects.filter(user_projects__notification__isnull=False):
        res[user.username] = {}
        for up in user.user_projects.filter(notification=True):
            current_milestones = list(up.project.allowed_milestones.filter(is_current=True).values_list('milestone_name', flat=True))
            current_milestone = current_milestones[0] if current_milestones else None
            if not current_milestone:
                continue
            current_ticket_ids = list(Ticket.objects.filter(milestone=current_milestone).values_list('id', flat=True))

            # Новые тикеты

            new_project_changes = trac_models.TicketChange.objects.filter(field__in=['status', 'milestone', 'owner']).filter(ticket__in=current_ticket_ids)
            # Тикеты, которые ушли из milestone
            left_from_milestone_tickets = trac_models.TicketChange.objects.filter(
                Q(field='milestone')&Q(oldvalue=current_milestone)&~Q(newvalue=current_milestone)
            )
            new_tickets = []
            left_tickets = []

            for ticket_change in new_project_changes:
                find_notification = Notification.objects.filter(change_time=ticket_change.time, ticket=ticket_change.ticket).exists()
                if not find_notification:
                    new_tickets.append(ticket_change)
            for ticket_change in left_from_milestone_tickets:
                find_notification = Notification.objects.filter(change_time=ticket_change.time, ticket=ticket_change.ticket).exists()
                if not find_notification:
                    left_tickets.append(ticket_change)


            res[user.username][up.project.name] = {
                'new_tickets': new_tickets,
                'left_tickets': left_tickets,
                'current_milestone': current_milestones
            }

    return res





class Command(BaseCommand):
    args = ''
    help = u'проверяем по всем ли тикетам были высланы уведомления, возвращаем те, по которым не высланы.'

    def handle(self, *args, **options):

        mailing_info = get_mailing_info()
        for user, all_tickets in mailing_info.iteritems():
            html_message = render_to_string('djtrac/simple_email.html', {'all_tickets': all_tickets})
            sended = send_mail('Subject here', html_message, 'mai@gmail.com', ['g10k.info@gmail.com'], fail_silently=False, html_message=html_message)
            if sended:
                save_user_tickets(user, all_tickets.get('left_tickets'), all_tickets.get('new_tickets'))



