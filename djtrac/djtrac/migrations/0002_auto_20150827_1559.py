# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djtrac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('owner', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'component',
                'managed': True if 'test' in sys.argv else False,
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('due', models.IntegerField(null=True, blank=True)),
                ('completed', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'milestone',
                'managed': True if 'test' in sys.argv else False,
            },
        ),
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notificated_milestone', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u0430\u043f\u0430, \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0430\u043b \u0442\u0438\u043a\u0435\u0442 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438.', choices=[('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"'), ('\u041f\u0440\u043e\u0444', '\u041f\u0440\u043e\u0444'), ('\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"', '\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"'), ('\u041b\u041c\u041a', '\u041b\u041c\u041a'), ('\u0412\u044b\u0435\u0437\u0434 \u041b\u041c\u041a', '\u0412\u044b\u0435\u0437\u0434 \u041b\u041c\u041a'), ('\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', '\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c'), ('\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440', '\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440'), ('soft-way site', 'soft-way site'), ('\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444', '\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444'), ('\u041c\u0418\u0421 \u041c\u041c', '\u041c\u0418\u0421 \u041c\u041c'), ('CRM', 'CRM'), ('uniorder', 'uniorder'), ('matrix', 'matrix'), ('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0'), ('uniorder2', 'uniorder2'), ('MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430', 'MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430'), ('MIS MM \u041a\u041a', 'MIS MM \u041a\u041a'), ('MIS MM \u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', 'MIS MM \u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), ('roster', 'roster'), ('\u041c\u0418\u0421 \u041c\u041c 2015-05', '\u041c\u0418\u0421 \u041c\u041c 2015-05'), ('\u041c\u0418\u0421 \u041c\u041c 2015-06', '\u041c\u0418\u0421 \u041c\u041c 2015-06'), ('\u041c\u0418\u0421 \u041c\u041c 2015-07', '\u041c\u0418\u0421 \u041c\u041c 2015-07'), ('\u041c\u0418\u0421 \u041c\u041c 2015-08', '\u041c\u0418\u0421 \u041c\u041c 2015-08'), ('\u041c\u0418\u0421 \u041c\u041c 2015-09', '\u041c\u0418\u0421 \u041c\u041c 2015-09')])),
                ('ticket', models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0438\u043a\u0435\u0442\u0430 \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0431\u044b\u043b\u043e \u043e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u0435')),
                ('dc', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f, \u043a\u043e\u0433\u0434\u0430 \u0432\u044b\u0441\u043b\u0430\u043d\u043e \u043e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u0435(\u043f\u0438\u0441\u044c\u043c\u043e)')),
                ('user', models.ForeignKey(related_name='notification_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439 (\u043f\u0438\u0441\u0435\u043c)',
                'verbose_name_plural': '\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439 (\u043f\u0438\u0441\u0435\u043c)',
            },
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification', models.BooleanField(default=False, verbose_name='\u041e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u043f\u043e \u043f\u043e\u0447\u0442\u0435')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.AlterField(
            model_name='projectcomponent',
            name='component_name',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u0430', choices=[('CRM', 'CRM'), ('lab_costs', 'lab_costs'), ('store', 'store'), ('\u0412\u044b\u0435\u0437\u0434\u044b', '\u0412\u044b\u0435\u0437\u0434\u044b'), ('\u041b\u041c\u041a', '\u041b\u041c\u041a'), ('\u041c\u0418\u0421 \u041c\u041c', '\u041c\u0418\u0421 \u041c\u041c'), ('\u041f\u0420\u041e\u0424', '\u041f\u0420\u041e\u0424'), ('\u041f\u043e\u0440\u0442\u0430\u043b', '\u041f\u043e\u0440\u0442\u0430\u043b'), ('\u0420\u0435\u0435\u0441\u0442\u0440', '\u0420\u0435\u0435\u0441\u0442\u0440')]),
        ),
        migrations.AlterField(
            model_name='projectmilestone',
            name='milestone_name',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u0430\u043f\u0430', choices=[('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"'), ('\u041f\u0440\u043e\u0444', '\u041f\u0440\u043e\u0444'), ('\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"', '\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"'), ('\u041b\u041c\u041a', '\u041b\u041c\u041a'), ('\u0412\u044b\u0435\u0437\u0434 \u041b\u041c\u041a', '\u0412\u044b\u0435\u0437\u0434 \u041b\u041c\u041a'), ('\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', '\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c'), ('\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440', '\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440'), ('soft-way site', 'soft-way site'), ('\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444', '\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444'), ('\u041c\u0418\u0421 \u041c\u041c', '\u041c\u0418\u0421 \u041c\u041c'), ('CRM', 'CRM'), ('uniorder', 'uniorder'), ('matrix', 'matrix'), ('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0'), ('uniorder2', 'uniorder2'), ('MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430', 'MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430'), ('MIS MM \u041a\u041a', 'MIS MM \u041a\u041a'), ('MIS MM \u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', 'MIS MM \u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), ('roster', 'roster'), ('\u041c\u0418\u0421 \u041c\u041c 2015-05', '\u041c\u0418\u0421 \u041c\u041c 2015-05'), ('\u041c\u0418\u0421 \u041c\u041c 2015-06', '\u041c\u0418\u0421 \u041c\u041c 2015-06'), ('\u041c\u0418\u0421 \u041c\u041c 2015-07', '\u041c\u0418\u0421 \u041c\u041c 2015-07'), ('\u041c\u0418\u0421 \u041c\u041c 2015-08', '\u041c\u0418\u0421 \u041c\u041c 2015-08'), ('\u041c\u0418\u0421 \u041c\u041c 2015-09', '\u041c\u0418\u0421 \u041c\u041c 2015-09')]),
        ),
        migrations.AddField(
            model_name='userproject',
            name='project',
            field=models.ForeignKey(to='djtrac.Project'),
        ),
        migrations.AddField(
            model_name='userproject',
            name='user',
            field=models.ForeignKey(related_name='user_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='user_projects',
            field=models.ManyToManyField(related_name='allowed_projects', through='djtrac.UserProject', to=settings.AUTH_USER_MODEL),
        ),
    ]
