# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20161122_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprod',
            name='object_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]