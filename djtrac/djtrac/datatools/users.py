# -*- encoding: utf-8 -*-
from djtrac.models.trac_models import Ticket


def components_for_user(user):
    """
    :param user: django.contrib.auth.models.User
    :return: set названий компонент
    """
    projects = user.allowed_projects.all()
    components = set()
    for project in projects:
        components.update(project.allowed_components.values_list('component', flat=True))
    return components


def get_user_milestones(user, only_notification=False):
    projects = [up.project for up in user.user_projects.filter(notification=True)] \
        if only_notification else user.allowed_projects.all()
    milestones = set()
    for project in projects:
        milestones.update(list(project.allowed_milestones.values_list('milestone', flat=True)))
    return milestones


def get_user_tickets(user, only_notification=False):
    tickets = []
    user_projects = user.user_projects.filter(notification=True) if only_notification else user.user_projects.all()
    for up in user_projects:
        current_milestones = list(up.project.allowed_milestones.
                                  filter(is_current=True).values_list('milestone', flat=True))
        tickets.extend(list(Ticket.objects.filter(milestone__in=current_milestones).values_list('id', flat=True)))
    return tickets
