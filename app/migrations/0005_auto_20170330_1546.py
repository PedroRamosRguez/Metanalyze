# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170330_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='nObjetives',
            new_name='nObjectives',
        ),
    ]
