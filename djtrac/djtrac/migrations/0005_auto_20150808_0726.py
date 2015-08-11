# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djtrac', '0004_auto_20150804_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component', models.ForeignKey(verbose_name='\u041a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442', to='djtrac.ComponentInMysql')),
                ('user', models.ForeignKey(related_name='allowed_components', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0430\u0432\u043e \u043d\u0430 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442',
                'verbose_name_plural': '\u041f\u0440\u0430\u0432\u0430 \u043d\u0430 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.RemoveField(
            model_name='permissionreport',
            name='component',
        ),
        migrations.RemoveField(
            model_name='permissionreport',
            name='user',
        ),
        migrations.DeleteModel(
            name='PermissionReport',
        ),
    ]
