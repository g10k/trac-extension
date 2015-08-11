# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djtrac', '0005_auto_20150808_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('owner', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('users', models.ManyToManyField(related_name='allowed_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProjectComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component_name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u0430', choices=[('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'), ('\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435', '\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), ('\u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'), ('\u041f\u0420\u041e\u0424', '\u041f\u0420\u041e\u0424'), ('\u041b\u041c\u041a', '\u041b\u041c\u041a'), ('\u041c\u0418\u0421 \u041c\u041c', '\u041c\u0418\u0421 \u041c\u041c'), ('CRM', 'CRM'), ('\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435', '\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435'), ('\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435', '\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), ('\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435', '\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435'), ('\u0412\u044b\u0435\u0437\u0434\u044b', '\u0412\u044b\u0435\u0437\u0434\u044b'), ('\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f', '\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f'), ('\u0420\u0435\u0435\u0441\u0442\u0440', '\u0420\u0435\u0435\u0441\u0442\u0440'), ('\u041f\u043e\u0440\u0442\u0430\u043b', '\u041f\u043e\u0440\u0442\u0430\u043b')])),
                ('project', models.ForeignKey(related_name='allowed_components', to='djtrac.Project')),
            ],
            options={
                'verbose_name': 'ProjectComponent',
                'verbose_name_plural': 'ProjectComponent',
            },
        ),
    ]
