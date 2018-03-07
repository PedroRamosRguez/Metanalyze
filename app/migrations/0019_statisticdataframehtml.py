# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20170603_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticDataframeHtml',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listValues', app.models.ListField()),
                ('configuration', models.ForeignKey(to='app.Configuration')),
            ],
        ),
    ]
