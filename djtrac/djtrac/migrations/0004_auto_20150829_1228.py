# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djtrac', '0003_auto_20150828_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notificated_milestone', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u0430\u043f\u0430, \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0430\u043b \u0442\u0438\u043a\u0435\u0442 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438.')),
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
            name='UserTicketNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0438\u043a\u0435\u0442\u0430, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0431\u044b\u043b\u043e \u0432\u044b\u0441\u043b\u0430\u043d\u043e \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435')),
                ('user', models.ForeignKey(related_name='last_notified_tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0422\u0438\u043a\u0435\u0442',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0422\u0438\u043a\u0435\u0442\u044b',
            },
        ),
        migrations.RemoveField(
            model_name='notificationhistory',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='component',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='projectcomponent',
            name='component_name',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='projectmilestone',
            name='milestone_name',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u0430\u043f\u0430'),
        ),
        migrations.DeleteModel(
            name='NotificationHistory',
        ),
    ]
