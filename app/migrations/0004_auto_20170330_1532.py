# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_algorithms_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithms',
            old_name='nvariablesAlgorithm',
            new_name='nVariablesAlgorithm',
        ),
        migrations.RemoveField(
            model_name='algorithms',
            name='nAlgorithms',
        ),
        migrations.AddField(
            model_name='configuration',
            name='nAlgorithms',
            field=models.CharField(default=datetime.datetime(2017, 3, 30, 15, 32, 28, 104211, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
