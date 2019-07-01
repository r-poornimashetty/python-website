# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_auto_20190620_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterDegreeStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterdegreestream', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='masterdegreestream',
            field=models.CharField(choices=[('-none-', '-none-'), ('M.Tech', 'M.Tech'), ('M.E', 'M.E'), ('MSC', 'MSC'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('MPhil', 'MPhil'), ('MA', 'MA'), ('MSW', 'MSW'), ('MHM', 'MHM'), ('MCOM', 'MCOM'), ('Other', 'Other')], default='none', max_length=20, verbose_name='Matser Degree Stream'),
        ),
    ]