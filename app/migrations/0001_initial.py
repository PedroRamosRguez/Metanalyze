# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nAlgorithms', models.CharField(max_length=100)),
                ('algorithm', models.CharField(max_length=100)),
                ('idAlgorithm', models.CharField(max_length=100)),
                ('fileName', models.CharField(max_length=100)),
                ('nvariablesAlgorithm', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test', models.CharField(max_length=100)),
                ('nObjetives', models.CharField(max_length=100)),
                ('nExecutions', models.CharField(max_length=100)),
                ('step', models.CharField(max_length=100)),
                ('stopCondition', models.CharField(max_length=100)),
                ('dataOutput', models.CharField(max_length=100)),
                ('bound', models.CharField(max_length=100)),
                ('metric', models.CharField(max_length=100)),
            ],
        ),
    ]
