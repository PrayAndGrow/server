# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainfood', '0003_auto_20160409_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='brain_bits',
        ),
        migrations.AddField(
            model_name='brainbit',
            name='brain_bits',
            field=models.ManyToManyField(to='brainfood.Tag'),
        ),
    ]
