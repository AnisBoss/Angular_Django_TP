# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='body',
            new_name='Brand',
        ),
        migrations.RemoveField(
            model_name='note',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='note',
            name='title',
        ),
        migrations.AddField(
            model_name='note',
            name='Description',
            field=models.TextField(default='blabla'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='Path',
            field=models.TextField(default='balbal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='Price',
            field=models.TextField(default='blabal'),
            preserve_default=False,
        ),
    ]
