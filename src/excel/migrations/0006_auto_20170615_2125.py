# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0005_auto_20170615_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excel.Unidade'),
        ),
    ]
