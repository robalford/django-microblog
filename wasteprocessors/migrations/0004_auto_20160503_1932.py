# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0003_wasteprocessor_materials_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wasteprocessor',
            name='accepts_salvage',
        ),
        migrations.RemoveField(
            model_name='wasteprocessor',
            name='accepts_scrap',
        ),
        migrations.RemoveField(
            model_name='wasteprocessor',
            name='accepts_surplus',
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='waste_types_accepted',
            field=models.ManyToManyField(related_name='waste_types', to='wasteprocessors.WasteType'),
        ),
    ]
