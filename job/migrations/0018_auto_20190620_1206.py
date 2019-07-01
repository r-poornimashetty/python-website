# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 12:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_auto_20190620_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DegreeStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dstream', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DiplomaStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diplomastream', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='student',
            name='degree',
            field=models.CharField(choices=[('-none-', '-none-'), ('BE', 'BE'), ('BSC', 'BSC'), ('BCA', 'BCA'), ('BECOM', 'BECOM'), ('BTECH', 'BETEC'), ('BBM', 'BBM'), ('BA', 'BA')], default='none', max_length=20, verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='student',
            name='pincode',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Pincode'),
        ),
        migrations.AddField(
            model_name='student',
            name='puc_diploma_year',
            field=models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=job.models.current_year, null=True, verbose_name='year'),
        ),
        migrations.AddField(
            model_name='student',
            name='sate',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='select', max_length=20, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='student',
            name='twelthboard',
            field=models.CharField(choices=[('None', 'None'), ('Puc/12th', 'Puc/12th'), ('Diploma', 'Diploma'), ('ITI', 'ITI')], default='none', max_length=20, verbose_name='12th board'),
        ),
        migrations.AddField(
            model_name='student',
            name='Diplomastream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.DiplomaStream'),
        ),
        migrations.AddField(
            model_name='student',
            name='degreecollege',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.College'),
        ),
        migrations.AddField(
            model_name='student',
            name='degreestream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.DegreeStream'),
        ),
    ]
