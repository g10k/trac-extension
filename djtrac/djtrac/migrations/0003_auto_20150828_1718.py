# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0002_auto_20150827_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketChange',
            fields=[
                ('ticket', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('field', models.TextField(null=True, blank=True)),
                ('oldvalue', models.TextField(null=True, blank=True)),
                ('newvalue', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ticket_change',
                'managed': True if 'test' in sys.argv else False,
            },
        ),
        migrations.AddField(
            model_name='notificationhistory',
            name='change_time',
            field=models.IntegerField(default=1, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectcomponent',
            name='component_name',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u0430', choices=[('\u041c\u0418\u0421 \u041c\u041c', '\u041c\u0418\u0421 \u041c\u041c'), ('\u041f\u0420\u041e\u0424', '\u041f\u0420\u041e\u0424'), ('\u041b\u041c\u041a', '\u041b\u041c\u041a'), ('CRM', 'CRM'), ('\u0420\u0435\u0435\u0441\u0442\u0440', '\u0420\u0435\u0435\u0441\u0442\u0440'), ('\u0412\u044b\u0435\u0437\u0434\u044b', '\u0412\u044b\u0435\u0437\u0434\u044b'), ('\u041f\u043e\u0440\u0442\u0430\u043b', '\u041f\u043e\u0440\u0442\u0430\u043b'), ('lab_costs', 'lab_costs'), ('store', 'store'), ('\u043b\u0430\u0431\u0430', '\u043b\u0430\u0431\u0430')]),
        ),
    ]
