# coding: utf-8
from django.db.models.aggregates import Max
from django.template.loader import render_to_string
from django.utils import timezone
import lxml.html
from django.core.mail import send_mail
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
def send_mails(request):
    c = {}

    milestone = request.GET['milestone']

    milestone_tickets = models.Ticket.objects.\
        filter(milestone=milestone).\
        values_list('id', flat=True)
    milestone_tickets = list(milestone_tickets)

    notes = models.TicketReleaseNote.objects.\
        filter(ticket__in=milestone_tickets).\
        exclude(description='')

    user_notes = {}
    group_notes = {}
    for note in notes:
        for user in note.target_users.all():
            user_notes.setdefault(user, []).append(note)
        for group in note.target_groups.all():
            group_notes.setdefault(group, []).append(note)

    c['user_notes'] = user_notes
    c['group_notes'] = group_notes
    c['latest_mail_dt'] = notes.aggregate(latest_mail_dt=Max('mail_dt'))['latest_mail_dt']

    if request.POST:
        _send_release_notes(milestone, notes)
        return redirect(request.GET.get('next', reverse('djtrac.views.main.main')))

    return render(request, 'djtrac/release_note/send_mail.html', c)


def _send_release_notes(milestone, notes):
    users_notes = {}
    for note in notes:
        for user in note.get_target_users():
            users_notes.setdefault(user, []).append(note)

    for user, user_notes in users_notes.items():
        recipient_list = [user.email]
        from_email = settings.EMAIL_HOST_USER
        subject = u'Замечания к релизу "%s"' % milestone

        html_content = render_to_string(
            'djtrac/release_note/mail_template.html',
            {'milestone': milestone, 'notes': user_notes}
        )

        text_content = lxml.html.fromstring(html_content).text_content()

        send_mail(
            subject, text_content, html_message=html_content,
            from_email=from_email, recipient_list=recipient_list,
            fail_silently=False,
        )

        notes.update(mail_dt=timezone.now())
