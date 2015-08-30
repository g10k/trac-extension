# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import sys


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('type', models.TextField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('changetime', models.IntegerField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f', blank=True)),
                ('component', models.TextField(null=True, blank=True)),
                ('severity', models.TextField(null=True, blank=True)),
                ('priority', models.TextField(null=True, blank=True)),
                ('owner', models.TextField(null=True, blank=True)),
                ('reporter', models.TextField(null=True, blank=True)),
                ('cc', models.TextField(null=True, blank=True)),
                ('version', models.TextField(null=True, blank=True)),
                ('milestone', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('resolution', models.TextField(null=True, blank=True)),
                ('summary', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('keywords', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ticket',
                 'managed': True if 'test' in sys.argv else False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('users', models.ManyToManyField(related_name='allowed_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProjectComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component_name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u0430', choices=[('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'), ('\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435', '\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), ('\u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'), ('\u041f\u0420\u041e\u0424', '\u041f\u0420\u041e\u0424'), ('\u041b\u041c\u041a', '\u041b\u041c\u041a'), ('\u041c\u0418\u0421 \u041c\u041c', '\u041c\u0418\u0421 \u041c\u041c'), ('CRM', 'CRM'), ('\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435', '\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435'), ('\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435', '\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), ('\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435', '\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435'), ('\u0412\u044b\u0435\u0437\u0434\u044b', '\u0412\u044b\u0435\u0437\u0434\u044b'), ('\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f', '\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f'), ('\u0420\u0435\u0435\u0441\u0442\u0440', '\u0420\u0435\u0435\u0441\u0442\u0440'), ('\u041f\u043e\u0440\u0442\u0430\u043b', '\u041f\u043e\u0440\u0442\u0430\u043b')])),
                ('project', models.ForeignKey(related_name='allowed_components', to='djtrac.Project')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442 \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435',
                'verbose_name_plural': '\u041a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u044b \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435',
            },
        ),
        migrations.CreateModel(
            name='ProjectMilestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('milestone_name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u0430\u043f\u0430', choices=[('', ''), ('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"'), ('\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"', '\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"'), ('\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', '\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c'), ('\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440', '\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440'), ('soft-way site', 'soft-way site'), ('\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444', '\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444'), ('uniorder', 'uniorder'), ('matrix', 'matrix'), ('MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430', 'MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430'), ('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0'), ('uniorder2', 'uniorder2'), ('MIS MM \u041a\u041a', 'MIS MM \u041a\u041a'), ('\u041c\u0418\u0421 \u041c\u041c 2015-07', '\u041c\u0418\u0421 \u041c\u041c 2015-07'), ('\u041c\u0418\u0421 \u041c\u041c 2015-05', '\u041c\u0418\u0421 \u041c\u041c 2015-05'), ('\u041c\u0418\u0421 \u041c\u041c 2015-06', '\u041c\u0418\u0421 \u041c\u041c 2015-06')])),
                ('is_current', models.BooleanField(default=False, verbose_name='\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u044d\u0442\u0430\u043f')),
                ('project', models.ForeignKey(related_name='allowed_milestones', to='djtrac.Project')),
            ],
            options={
                'verbose_name': '\u042d\u0442\u0430\u043f \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435',
                'verbose_name_plural': '\u042d\u0442\u0430\u043f\u044b \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435',
            },
        ),
    ]
