# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0002_auto_20150827_1559'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='targetgroup',
            name='users',
            field=models.ManyToManyField(to='djtrac.TargetUser', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438'),
        ),
        migrations.AddField(
            model_name='project',
            name='target_groups',
            field=models.ManyToManyField(to='djtrac.TargetGroup', verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='project',
            name='target_users',
            field=models.ManyToManyField(to='djtrac.TargetUser', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0'),
        ),
    ]
