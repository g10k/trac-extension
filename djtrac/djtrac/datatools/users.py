# -*- encoding: utf-8 -*-
def components_for_user(user):
    """
    :param user: django.contrib.auth.models.User
    :return: set названий компонент
    """
    projects = user.allowed_projects.all()
    components = set()
    for project in projects:
        components.update(project.allowed_components.values_list('component_name', flat=True))
    return components


def milestones_for_user(user):
    """
    :param user: django.contrib.auth.models.User
    :return: set названий компонент
    """
    projects = user.allowed_projects.all()
    milestones = set()
    for project in projects:
        milestones.update(project.allowed_milestones.values_list('milestone_name', flat=True))
    return milestones