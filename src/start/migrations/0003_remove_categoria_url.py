# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_auto_20170511_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='url',
        ),
    ]
