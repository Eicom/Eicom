# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje',
            field=models.TextField(max_length=300),
        ),
    ]
