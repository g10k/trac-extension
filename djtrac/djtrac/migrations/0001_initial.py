# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('type', models.TextField(null=True, blank=True)),
                ('id', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('filename', models.TextField(null=True, blank=True)),
                ('size', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('ipnr', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attachment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthCookie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cookie', models.TextField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('ipnr', models.TextField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'auth_cookie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('generation', models.IntegerField(null=True, blank=True)),
                ('key', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cache',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('owner', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'component',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.TextField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'enum',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('due', models.IntegerField(null=True, blank=True)),
                ('completed', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'milestone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NodeChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repos', models.IntegerField(null=True, blank=True)),
                ('rev', models.TextField(null=True, blank=True)),
                ('path', models.TextField(null=True, blank=True)),
                ('node_type', models.TextField(null=True, blank=True)),
                ('change_type', models.TextField(null=True, blank=True)),
                ('base_path', models.TextField(null=True, blank=True)),
                ('base_rev', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'node_change',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField(null=True, blank=True)),
                ('action', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('query', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'repository',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repos', models.IntegerField(null=True, blank=True)),
                ('rev', models.TextField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'revision',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.TextField(null=True, blank=True)),
                ('authenticated', models.IntegerField(null=True, blank=True)),
                ('last_visit', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SessionAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.TextField(null=True, blank=True)),
                ('authenticated', models.IntegerField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'session_attribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'system',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('type', models.TextField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('changetime', models.IntegerField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f', blank=True)),
                ('component', models.TextField(null=True, blank=True)),
                ('severity', models.TextField(null=True, blank=True)),
                ('priority', models.TextField(null=True, blank=True)),
                ('owner', models.TextField(null=True, blank=True)),
                ('reporter', models.TextField(null=True, blank=True)),
                ('cc', models.TextField(null=True, blank=True)),
                ('version', models.TextField(null=True, blank=True)),
                ('milestone', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('resolution', models.TextField(null=True, blank=True)),
                ('summary', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('keywords', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TicketChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('field', models.TextField(null=True, blank=True)),
                ('oldvalue', models.TextField(null=True, blank=True)),
                ('newvalue', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ticket_change',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TicketCustom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.IntegerField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ticket_custom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('author', models.TextField(null=True, blank=True)),
                ('ipnr', models.TextField(null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('readonly', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'wiki',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComponentInMysql',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('owner', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component', models.ForeignKey(verbose_name='\u041a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442', to='djtrac.ComponentInMysql')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
