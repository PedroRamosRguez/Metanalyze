# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_algorithms_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithms',
            name='fileName',
            field=models.CharField(default=datetime.datetime(2017, 3, 30, 11, 12, 40, 348608, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
