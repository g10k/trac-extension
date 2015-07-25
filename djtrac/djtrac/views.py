# -*- encoding: utf-8 -*-
from django.shortcuts import render
from djtrac.models import Milestone, Ticket
from djtrac.forms import ReportForm
from djtrac.utils import timestamp_from_date
from djtrac.datatools.reports import get_allowed_tickets


def main(request):
    form = ReportForm(request.GET or None)
    tickets = []
    if form.is_valid():
        milestone = form.cleaned_data.get('milestone')
        number = form.cleaned_data.get('number')
        keyword = form.cleaned_data.get('keyword')
        dt_from = form.cleaned_data.get('dt_from')
        dt_to = form.cleaned_data.get('dt_to')

        tickets = Ticket.objects.all().order_by('-time')
        tickets = get_allowed_tickets('g10k', tickets)
        if milestone:
            tickets = Ticket.objects.filter(milestone=milestone)
        if keyword:
            tickets = tickets.filter(keywords__icontains=keyword)
        if dt_from:
            tickets = tickets.filter(time__gte=timestamp_from_date(dt_from))
        if dt_to:
            tickets = tickets.filter(time__lte=timestamp_from_date(dt_to))
        if number:
            tickets = Ticket.objects.filter(id=number)

    else:
        pass
    c = {
        'milestones': Milestone.objects.all(),
        'form': form,
        'tickets': tickets
    }
    return render(request, 'index.html', c)

