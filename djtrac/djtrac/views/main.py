# -*- encoding: utf-8 -*-
from collections import OrderedDict
from django.shortcuts import render
from django.views import generic

from djtrac.models import Milestone, Ticket, TicketChangeInMysql, TicketChange
from djtrac.forms import ReportForm, TicketForm
from djtrac.utils import timestamp_from_date
from djtrac.datatools.reports import prepare_sort_params, get_page


def main(request):
    print request.user
    sort_key = ''
    form = ReportForm(request.GET or None, user=request.user)
    tickets = []
    group_by_components = None
    group_by_milestone = None
    result = {}
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

        # tickets = Ticket.objects.all().order_by('-time')
        tickets = Ticket.objects.get_allowed(request.user).order_by('-time')
        # tickets = get_allowed_tickets('g10k', tickets)
        if milestone:
            tickets = Ticket.objects.filter(milestone=milestone)
        if component:
            tickets = Ticket.objects.filter(component=component)
        if keyword:
            tickets = tickets.filter(keywords__icontains=keyword)
        if dt_from:
            tickets = tickets.filter(time__gte=timestamp_from_date(dt_from))
        if dt_to:
            tickets = tickets.filter(time__lte=timestamp_from_date(dt_to))
        if number:
            tickets = Ticket.objects.filter(id=number)
        sort_key = request.GET.get('sort', '-time')
        tickets = tickets.order_by(sort_key)


        # Логика группировок

        if group_by_components and group_by_milestone:
            result = OrderedDict()

            components = set(tickets.values_list('component', flat=True).distinct()) - set((''))
            milestones = set(tickets.values_list('milestone', flat=True).distinct()) - set((''))
            print milestones
            for component in components:
                result[component] = OrderedDict()
                for milestone in milestones:
                    key = milestones
                    if tickets.filter(component=component, milestone=milestone).exists():
                        result[component][milestone] = get_page(request, tickets.filter(component=component, milestone=milestone), 20)

            import pprint
            pprint.pprint(result)

        elif group_by_components:
            result = OrderedDict()
            components = list(tickets.values_list('component', flat=True).distinct())
            for component in components:
                result[component] = get_page(request, tickets.filter(component=component), 20)



    else:
        pass
    c = {
        'milestones': Milestone.objects.all(),
        'form': form,
        'tickets': tickets,
        'sort_key': sort_key.replace('-', ''),
        'sort_params': prepare_sort_params(
            ('id', 'summary', 'time', 'changetime', 'milestone','priority', 'owner','status','keywords'),request
        ),
        'page': get_page(request, tickets, 100),
        'group_by_components': group_by_components,
        'group_by_milestone': group_by_milestone,
        'tickets_by_components': result
    }

    return render(request, 'djtrac/index.html', c)


class TicketDetail(generic.DetailView):
    model = Ticket
    # form = TicketForm
    template_name = 'djtrac/ticket_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TicketDetail, self).get_context_data(**kwargs)
        context['changes'] = TicketChangeInMysql.objects.filter(ticket=context['object'].id)
        context['form'] = TicketForm(instance=context['object'])
        # context['object2'] = TicketChange.objects.get(pk=context['object'].id)
        return context