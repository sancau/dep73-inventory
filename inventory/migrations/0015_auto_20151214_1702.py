# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20151210_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscitem',
            name='actual_placement',
            field=models.CharField(max_length=200, verbose_name='Фактическое расположение'),
        ),
    ]