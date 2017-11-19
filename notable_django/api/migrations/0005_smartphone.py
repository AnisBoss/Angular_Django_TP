# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tablet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.TextField()),
                ('Description', models.TextField()),
                ('Brand', models.TextField()),
                ('Path', models.TextField()),
            ],
        ),
    ]
