# -*- encoding: utf-8 -*-
from djtrac.models import Ticket
from django.conf import settings


def get_allowed_tickets(user, tickets=None):
    if not tickets:
        tickets = Ticket.objects.order_by('-time')
    perms = settings.COMPONENT_PERMISSIONS
    allowed_components = perms.get(user,'')
    if allowed_components == 'all':
        return tickets
    elif allowed_components == '':
        return Ticket.objects.none()
    else:
        tickets = tickets.filter(component__in=allowed_components)
        return tickets