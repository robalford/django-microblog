# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0007_auto_20160510_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='wasteprocessor',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]