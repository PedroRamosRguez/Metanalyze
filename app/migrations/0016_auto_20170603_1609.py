# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_statisticdataframetex_statisticdataframetxt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithms',
            old_name='hypervolumeValues',
            new_name='hypervolumeValue',
        ),
    ]
