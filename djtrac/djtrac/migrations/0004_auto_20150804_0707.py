# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from djtrac.templatetags.djtrac_tags import to_datetime

def copy_ticket_change(apps, schema_editor):
    TicketChange = apps.get_model('djtrac', 'TicketChange')
    TicketChangeInMysql = apps.get_model('djtrac', 'TicketChangeInMysql')
    for ticketchange in TicketChange.objects.using('trac_db').values('ticket', 'time', 'author','field','oldvalue','newvalue'):
        tc, created = TicketChangeInMysql.objects.get_or_create(
            ticket=ticketchange['ticket'],
            time=to_datetime(ticketchange['time']),
            author=ticketchange['author'],
            field=ticketchange['field'],
            oldvalue=ticketchange['oldvalue'],
            newvalue=ticketchange['newvalue']
        )
        if created:
            message = u'Created... \033[92mOk\n'
        else:
            message = u'Already has... \033[94mOk\n'

class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0003_auto_20150804_0707'),
    ]

    operations = [
        migrations.RunPython(copy_ticket_change)
    ]
