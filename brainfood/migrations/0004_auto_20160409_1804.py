# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainfood', '0003_auto_20160409_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainbit',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
