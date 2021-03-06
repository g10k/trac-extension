# -*- encoding: utf-8 -*-
import urllib
from collections import OrderedDict
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from djtrac import models
from djtrac import forms
from djtrac.utils import timestamp_from_date, prepare_sort_params, get_page

@login_required(login_url='/login/')
def main(request):
    if not request.GET:
        current_milestone = models.ProjectMilestone.objects.filter(is_current=True).first()
        if current_milestone:
            return redirect(
                "%s?%s" % (reverse('djtrac.views.main.main'),
                           urllib.urlencode({'milestone': current_milestone.milestone.encode('utf-8')}))
            )
    form = forms.ReportForm(request.GET or None, user=request.user)
    tickets = []
    group_by_components = None
    group_by_milestone = None
    show_description = None
    grouped_tickets = OrderedDict()
    if form.is_valid():
        milestone = form.cleaned_data.get('milestone')
        component = form.cleaned_data.get('component')
        number = form.cleaned_data.get('number')
        keyword = form.cleaned_data.get('keyword')
        dt_from = form.cleaned_data.get('dt_from')
        dt_to = form.cleaned_data.get('dt_to')
        group_by_components = form.cleaned_data.get('group_by_components')
        group_by_milestone = form.cleaned_data.get('group_by_milestone')
        show_description = form.cleaned_data.get('show_description')

        tickets = models.Ticket.objects.get_allowed(request.user).\
            extra(select={
                'is_closed': "status='closed'",
                'priority_index': "case "
                                  "priority when 'низкий' then 1 "
                                  "when 'нормальный' then 2 "
                                  "when 'высокий' then 3 "
                                  "when 'блокирующий' then 4 "
                                  "end"
            }).\
            order_by('is_closed', '-priority_index')
        if milestone:
            tickets = tickets.filter(milestone=milestone)
        if component:
            tickets = tickets.filter(component=component)
        if keyword:
            tickets = tickets.filter(keywords__icontains=keyword)
        if dt_from:
            tickets = tickets.filter(time__gte=timestamp_from_date(dt_from))
        if dt_to:
            tickets = tickets.filter(time__lte=timestamp_from_date(dt_to))
        if number:
            tickets = tickets.filter(id=number)
        sort_key = request.GET.get('sort', None)
        if sort_key:
            tickets = tickets.order_by(sort_key)

        # Логика группировок
        components = set(tickets.values_list('component', flat=True).distinct()) - set((''))
        milestones = set(tickets.values_list('milestone', flat=True).distinct()) - set((''))
        if group_by_components and group_by_milestone:
            for component in components:
                grouped_tickets[component] = OrderedDict()
                for milestone in milestones:
                    if tickets.filter(component=component, milestone=milestone).exists():
                        grouped_tickets[component][milestone] = tickets.filter(component=component, milestone=milestone)

        elif group_by_components:
            for component in components:
                grouped_tickets[component] = tickets.filter(component=component)

        elif group_by_milestone:
            for milestone in milestones:
                grouped_tickets[milestone] = tickets.filter(milestone=milestone)

    have_release_notes = models.TicketReleaseNote.objects.filter(
        ticket__in=[t.id for t in tickets],
    ).filter(
        Q(target_users__isnull=False) | Q(target_groups__isnull=False)
    ).exclude(
        description=''
    ).exists()

    c = {
        'form': form,
        'tickets': tickets,
        'sort_params': prepare_sort_params(
            ('id', 'summary', 'time', 'changetime', 'milestone', 'priority_index', 'owner', 'status', 'keywords'),
            request
        ),
        'page': get_page(request, tickets, 100) if not group_by_components and not group_by_milestone else [],
        'group_by_components': group_by_components,
        'group_by_milestone': group_by_milestone,
        'grouped_tickets': grouped_tickets,
        'show_description': show_description,
        'HTTP_PATH_TO_TRAC': settings.HTTP_PATH_TO_TRAC,
        'have_release_notes': have_release_notes,
    }

    return render(request, 'djtrac/index.html', c)