# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrainBit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('type', models.CharField(choices=[('AR', 'Article'), ('VI', 'Video'), ('PO', 'Podcast')], max_length=2)),
                ('description', models.CharField(max_length=512)),
                ('image', models.URLField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='brainbit',
            name='tags',
            field=models.ManyToManyField(to='brainfood.Tag'),
        ),
    ]
