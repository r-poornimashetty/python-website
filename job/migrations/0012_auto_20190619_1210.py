# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-19 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20190619_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
    ]
