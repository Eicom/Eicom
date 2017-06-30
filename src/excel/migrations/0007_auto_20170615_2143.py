# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0006_auto_20170615_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excel.Familia'),
        ),
    ]