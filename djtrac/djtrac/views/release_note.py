# coding: utf-8
import urllib
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from djtrac import models
from djtrac import forms

@login_required(login_url='/login/')
def edit(request, ticket_id):
    c = {}

    qs = models.TicketReleaseNote.objects.filter(ticket=ticket_id)
    if qs:
        ticket_note = qs[0]
    else:
        ticket_note = models.TicketReleaseNote(ticket=ticket_id)

    form = forms.TicketReleaseNote(request.POST or None, instance=ticket_note)
    if form.is_valid():
        form.save()
        return redirect(request.GET.get('next', reverse('djtrac.views.main.main')))

    c['form'] = form
    return render(request, 'djtrac/release_note/edit.html', c)


@login_required(login_url='/login/')
def send_mail(request):
    c = {}

    milestone_name = request.GET['milestone']


    return render(request, 'djtrac/release_note/send_mail.html', c)