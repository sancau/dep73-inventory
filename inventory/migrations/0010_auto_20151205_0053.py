# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20151205_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='next_test_date',
            field=models.DateField(verbose_name='Срок поверки'),
        ),
    ]
