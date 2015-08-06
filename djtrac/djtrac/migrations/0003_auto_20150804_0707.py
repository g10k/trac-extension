# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0002_auto_20150725_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketChangeInMysql',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.IntegerField(null=True, blank=True)),
                ('time', models.DateTimeField(null=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('field', models.TextField(null=True, blank=True)),
                ('oldvalue', models.TextField(null=True, blank=True)),
                ('newvalue', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='permissionreport',
            options={'verbose_name': '\u041f\u0440\u0430\u0432\u043e \u043d\u0430 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442', 'verbose_name_plural': '\u041f\u0440\u0430\u0432\u0430 \u043d\u0430 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='permissionreport',
            name='user',
            field=models.ForeignKey(related_name='allowed_components', to=settings.AUTH_USER_MODEL),
        ),
    ]
