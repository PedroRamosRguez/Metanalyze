# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_chartsmodel_configuration'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgChartModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('configuration', models.ForeignKey(to='app.Configuration')),
            ],
        ),
        migrations.CreateModel(
            name='MaxChartModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('configuration', models.ForeignKey(to='app.Configuration')),
            ],
        ),
        migrations.CreateModel(
            name='MinAvgMaxChartModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('configuration', models.ForeignKey(to='app.Configuration')),
            ],
        ),
        migrations.CreateModel(
            name='MinChartModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('configuration', models.ForeignKey(to='app.Configuration')),
            ],
        ),
    ]
