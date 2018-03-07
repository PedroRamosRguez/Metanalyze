# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_algorithms_hypervolumevalues'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='anova',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
