# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170517_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithms',
            name='hypervolumeValues',
            field=app.models.ListField(default=1),
            preserve_default=False,
        ),
    ]
