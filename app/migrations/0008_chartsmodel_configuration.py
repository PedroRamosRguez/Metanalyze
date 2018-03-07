# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_chartsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartsmodel',
            name='configuration',
            field=models.ForeignKey(default=1, to='app.Configuration'),
            preserve_default=False,
        ),
    ]
