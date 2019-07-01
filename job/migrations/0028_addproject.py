# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0027_auto_20190621_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
            ],
        ),
    ]
