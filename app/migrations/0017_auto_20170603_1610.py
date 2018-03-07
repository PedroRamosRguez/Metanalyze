# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20170603_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithms',
            old_name='hypervolumeValue',
            new_name='hypervolumeValues',
        ),
    ]
