# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0003_auto_20150830_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketReleaseNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.IntegerField(verbose_name='\u0422\u0438\u043a\u0435\u0442')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('mail_dt', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043a\u043e\u0433\u0434\u0430 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435 \u0431\u044b\u043b\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e \u043f\u043e\u043b\u044c\u0437\u0432\u043e\u0430\u0442\u0435\u043b\u044f\u043c')),
                ('target_groups', models.ManyToManyField(help_text='\u043a \u043a\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0442\u0438\u043a\u0435\u0442\u0443', to='djtrac.TargetGroup', verbose_name='\u0413\u0440\u0443\u043f\u043f\u044b \u043f\u043e\u043b\u044c\u0437\u0432\u043e\u0430\u0442\u0435\u043b\u0435\u0439', blank=True)),
                ('target_users', models.ManyToManyField(help_text='\u043a \u043a\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0442\u0438\u043a\u0435\u0442\u0443', to='djtrac.TargetUser', verbose_name='\u041f\u043e\u043b\u044c\u0437\u0432\u043e\u0430\u0442\u0435\u043b\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u043b\u0438\u0437\u043d\u043e\u0443\u0442',
                'verbose_name_plural': '\u0420\u0435\u043b\u0438\u0437\u043d\u043e\u0443\u0442\u044b',
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='target_groups',
            field=models.ManyToManyField(to='djtrac.TargetGroup', verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='target_users',
            field=models.ManyToManyField(to='djtrac.TargetUser', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0', blank=True),
        ),
    ]
