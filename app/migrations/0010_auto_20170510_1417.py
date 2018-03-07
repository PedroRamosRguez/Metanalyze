# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_avgchartmodel_maxchartmodel_minavgmaxchartmodel_minchartmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='avgchartmodel',
            name='listValues',
            field=app.models.ListField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maxchartmodel',
            name='listValues',
            field=app.models.ListField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minavgmaxchartmodel',
            name='listValues',
            field=app.models.ListField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minchartmodel',
            name='listValues',
            field=app.models.ListField(default=1),
            preserve_default=False,
        ),
    ]
