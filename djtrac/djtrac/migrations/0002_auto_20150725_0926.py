# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.db import models, migrations

def copy_components(apps, schema_editor):
    Component = apps.get_model('djtrac', 'Component')
    ComponentInMysql = apps.get_model('djtrac', 'ComponentInMysql')
    print 'something'
    for component in Component.objects.using('trac_db').all():
        # ComponentInMysql(name)
        comp_mysql, created = ComponentInMysql.objects.get_or_create(
            name=component.name,
            owner=component.owner,
            description=component.description
        )
        if created:
            message = u'Created... \033[92mOk\n'
        else:
            message = u'Already has... \033[94mOk\n'
        sys.stdout.write(message)


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_components)
    ]
