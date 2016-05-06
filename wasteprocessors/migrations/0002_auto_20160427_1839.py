# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='material_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_type',
        ),
        migrations.RemoveField(
            model_name='waste',
            name='material',
        ),
        migrations.RemoveField(
            model_name='wasteprocessor',
            name='materials_accepted',
        ),
        migrations.AddField(
            model_name='materialtype',
            name='material_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waste',
            name='material_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wasteprocessors.MaterialType'),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='accepts_salvage',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='accepts_scrap',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='accepts_surplus',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='business_hours',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='paid_service',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='waste',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Project'),
        ),
        migrations.AlterField(
            model_name='wasteprocessor',
            name='address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='wasteprocessor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wasteprocessor',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='wasteprocessor',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='wasteprocessor',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectType',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]