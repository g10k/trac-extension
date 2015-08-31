# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djtrac', '0008_remove_projecttestserver_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserNotification',
            new_name='UserNotificationMilestoneChanges',
        ),
        migrations.AddField(
            model_name='usernotificationmilestonechanges',
            name='action',
            field=models.CharField(default='add', max_length=4, choices=[(b'add', b'add'), (b'left', b'left')]),
            preserve_default=False,
        ),
        migrations.AlterModelOptions(
            name='usernotificationmilestonechanges',
            options={'get_latest_by': 'mail_dt', 'verbose_name': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e', 'verbose_name_plural': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e'},
        ),
    ]
