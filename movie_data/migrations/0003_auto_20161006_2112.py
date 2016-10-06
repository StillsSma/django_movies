# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_data', '0002_auto_20161006_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='blank',
        ),
        migrations.AddField(
            model_name='ratings',
            name='rater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_data.Rater'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_data.Movies'),
        ),
    ]
