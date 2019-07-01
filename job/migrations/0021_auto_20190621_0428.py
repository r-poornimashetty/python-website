# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_auto_20190621_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Masterdegreesteam',
            new_name='Master_Degree_Stream',
        ),
        migrations.AlterField(
            model_name='student',
            name='masterdegree',
            field=models.CharField(choices=[('-none-', '-none-'), ('M.Tech', 'M.Tech'), ('M.E', 'M.E'), ('MSC', 'MSC'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('MPhil', 'MPhil'), ('MA', 'MA'), ('MSW', 'MSW'), ('MHM', 'MHM'), ('MCOM', 'MCOM'), ('Other', 'Other')], default='none', max_length=20, verbose_name='Matser Degree'),
        ),
    ]