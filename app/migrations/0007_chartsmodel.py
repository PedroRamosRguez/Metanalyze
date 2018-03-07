# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_algorithms_configuration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listValues', app.models.ListField()),
            ],
        ),
    ]
