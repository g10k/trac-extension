# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0005_auto_20150831_1529'),
    ]

    operations = [

        migrations.RenameField(
            model_name='userproject',
            old_name='notification',
            new_name='send_milestone_changes',
        ),

    ]
