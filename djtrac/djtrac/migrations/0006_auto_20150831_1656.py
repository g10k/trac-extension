# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0005_auto_20150831_1543'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='milestonerelease',
            name='planned_date',
            field=models.DateField(help_text='\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u0440\u0435\u043b\u0438\u0437\u0430', null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u043b\u0438\u0437\u0430', blank=True),
        ),
    ]
