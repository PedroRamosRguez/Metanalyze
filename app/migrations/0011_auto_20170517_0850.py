# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170510_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='bound',
            field=app.models.ListField(),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='metric',
            field=app.models.ListField(),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='test',
            field=app.models.ListField(),
        ),
    ]
