# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20170603_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='anova',
            new_name='statisticTest',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='test',
        ),
    ]
