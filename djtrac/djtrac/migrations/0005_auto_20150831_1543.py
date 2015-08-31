# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0004_auto_20150830_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilestoneRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('milestone', models.CharField(unique=True, max_length=255, verbose_name='\u042d\u0442\u0430\u043f')),
                ('planned_date', models.DateField(null=True, verbose_name='\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u0440\u0435\u043b\u0438\u0437\u0430')),
                ('mail_dt', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439')),
            ],
        ),
        migrations.AlterModelOptions(
            name='ticketreleasenote',
            options={'verbose_name': '\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f \u043a \u0432\u044b\u043f\u0443\u0441\u043a\u0443', 'verbose_name_plural': '\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f \u043a \u0432\u044b\u043f\u0443\u0441\u043a\u0443'},
        ),
        migrations.RemoveField(
            model_name='ticketreleasenote',
            name='mail_dt',
        ),
        migrations.AlterField(
            model_name='ticketreleasenote',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='ticketreleasenote',
            name='target_groups',
            field=models.ManyToManyField(help_text='\u043a \u043a\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0442\u0438\u043a\u0435\u0442\u0443', to='djtrac.TargetGroup', verbose_name='\u0413\u0440\u0443\u043f\u043f\u044b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='ticketreleasenote',
            name='target_users',
            field=models.ManyToManyField(help_text='\u043a \u043a\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0442\u0438\u043a\u0435\u0442\u0443', to='djtrac.TargetUser', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438', blank=True),
        ),
    ]
