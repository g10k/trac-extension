# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0006_auto_20150831_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilestoneRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('milestone', models.CharField(unique=True, max_length=255, verbose_name='\u042d\u0442\u0430\u043f')),
                ('planned_date', models.DateField(help_text='\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u0440\u0435\u043b\u0438\u0437\u0430', null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u043b\u0438\u0437\u0430', blank=True)),
                ('mail_dt', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTestServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('address', models.IPAddressField(verbose_name='IP \u0430\u0434\u0440\u0435\u0441')),
                ('url', models.URLField(verbose_name='http \u0430\u0434\u0440\u0435\u0441')),
                ('project', models.ForeignKey(verbose_name='\u041f\u0440\u043e\u0435\u043a\u0442', to='djtrac.Project')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u0441\u0435\u0440\u0432\u0435\u0440',
                'verbose_name_plural': '\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0435 \u0441\u0435\u0440\u0432\u0435\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='TargetGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='TargetUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('email', models.EmailField(max_length=254, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
                ('description', models.TextField(help_text='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0438 \u0442.\u043f.', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='TicketReleaseNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.IntegerField(verbose_name='\u0422\u0438\u043a\u0435\u0442')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('target_groups', models.ManyToManyField(help_text='\u043a \u043a\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0442\u0438\u043a\u0435\u0442\u0443', to='djtrac.TargetGroup', verbose_name='\u0413\u0440\u0443\u043f\u043f\u044b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439', blank=True)),
                ('target_users', models.ManyToManyField(help_text='\u043a \u043a\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0442\u0438\u043a\u0435\u0442\u0443', to='djtrac.TargetUser', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f \u043a \u0432\u044b\u043f\u0443\u0441\u043a\u0443',
                'verbose_name_plural': '\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f \u043a \u0432\u044b\u043f\u0443\u0441\u043a\u0443',
            },
        ),
        migrations.AlterField(
            model_name='userproject',
            name='send_milestone_changes',
            field=models.BooleanField(default=False, help_text='\u043e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u043e\u0431 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0441\u0442\u0430\u0432\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0445 \u044d\u0442\u0430\u043f\u043e\u0432 \u043f\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f', verbose_name='\u041e\u043f\u043e\u0432\u0435\u0449\u0430\u0442\u044c \u043e\u0431 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f\u0445'),
        ),
        migrations.AddField(
            model_name='targetgroup',
            name='users',
            field=models.ManyToManyField(to='djtrac.TargetUser', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438'),
        ),
        migrations.AddField(
            model_name='project',
            name='target_groups',
            field=models.ManyToManyField(to='djtrac.TargetGroup', verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='target_users',
            field=models.ManyToManyField(to='djtrac.TargetUser', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0', blank=True),
        ),
    ]
