# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-19 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_remove_student_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='DOB',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
    ]
