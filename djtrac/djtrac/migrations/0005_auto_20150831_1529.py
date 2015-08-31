# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djtrac', '0004_auto_20150829_1228'),
    ]

    operations = [
        migrations.RenameModel('UserTicketNotification', 'UserCurrentMilestoneTicket'),
        migrations.RenameModel('Notification', 'UserNotification'),

        migrations.AlterModelOptions(
            name='component',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'managed': False},
        ),
        migrations.RenameField(
            model_name='projectcomponent',
            old_name='component_name',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='projectmilestone',
            old_name='milestone_name',
            new_name='milestone',
        ),
        migrations.RenameField(
            model_name='usernotification',
            old_name='notificated_milestone',
            new_name='milestone',
        ),
        migrations.RenameField(
            model_name='usernotification',
            old_name='dc',
            new_name='mail_dt',
        ),
        migrations.AlterModelOptions(
            name='usercurrentmilestoneticket',
            options={},
        ),
        migrations.AlterModelOptions(
            name='usernotification',
            options={'verbose_name': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e', 'verbose_name_plural': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e'},
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='mail_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f, \u043a\u043e\u0433\u0434\u0430 \u0432\u044b\u0441\u043b\u0430\u043d\u043e \u043e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u0435 (\u043f\u0438\u0441\u044c\u043c\u043e)'),
        ),
    ]
