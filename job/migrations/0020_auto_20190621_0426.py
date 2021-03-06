# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_auto_20190621_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='masterdegreestream',
            new_name='masterdegree',
        ),
        migrations.AddField(
            model_name='student',
            name='Masterdegreesteam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.MasterDegreeStream'),
        ),
        migrations.AddField(
            model_name='student',
            name='masterdegreeoption',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=1, verbose_name='Have you done Master Degree?'),
        ),
    ]
