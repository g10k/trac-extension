# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djtrac', '0007_auto_20150831_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttestserver',
            name='address',
        ),
    ]
