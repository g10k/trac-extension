# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0007_projectmilestone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicketChangeInMysql',
        ),
        migrations.RemoveField(
            model_name='usercomponent',
            name='component',
        ),
        migrations.RemoveField(
            model_name='usercomponent',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='projectmilestone',
            options={'verbose_name': '\u042d\u0442\u0430\u043f \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435', 'verbose_name_plural': '\u042d\u0442\u0430\u043f\u044b \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435'},
        ),
        migrations.AlterField(
            model_name='projectmilestone',
            name='milestone_name',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u0430\u043f\u0430', choices=[('', ''), ('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438"'), ('\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"', '\u0418\u0421 "\u0421\u043a\u0440\u043e\u043f\u0438\u043e\u043d+"'), ('\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', '\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c'), ('\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440', '\u0410\u0418\u0421 \u0420\u0435\u0435\u0441\u0442\u0440'), ('soft-way site', 'soft-way site'), ('\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444', '\u0412\u044b\u0435\u0437\u0434\u043d \u041f\u0440\u043e\u0444'), ('uniorder', 'uniorder'), ('matrix', 'matrix'), ('MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430', 'MIS MM \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430'), ('\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0', '\u043f\u043e\u0440\u0442\u0430\u043b "\u041c\u0435\u0434\u043a\u043d\u0438\u0436\u043a\u0438" 3.0'), ('uniorder2', 'uniorder2'), ('MIS MM \u041a\u041a', 'MIS MM \u041a\u041a'), ('\u041c\u0418\u0421 \u041c\u041c 2015-07', '\u041c\u0418\u0421 \u041c\u041c 2015-07'), ('\u041c\u0418\u0421 \u041c\u041c 2015-05', '\u041c\u0418\u0421 \u041c\u041c 2015-05'), ('\u041c\u0418\u0421 \u041c\u041c 2015-06', '\u041c\u0418\u0421 \u041c\u041c 2015-06')]),
        ),
        migrations.DeleteModel(
            name='ComponentInMysql',
        ),
        migrations.DeleteModel(
            name='UserComponent',
        ),
    ]
