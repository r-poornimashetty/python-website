# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

CITY_CHOICES= [
    ('Select', 'Select'),
    ('Bangalore', 'Bangalore'),
    ('Kolar', 'Kolar'),
    ('Mysore', 'Mysore'),
    ('Mandya', 'Mandya'),
    ]

class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(("First Name"), max_length=100)
    lastname = models.CharField(("Last Name"), max_length=20,  null=True)
    semail = models.EmailField(("Email"))
    scontact = models.CharField(("Contact"), max_length=15)
    scity= models.CharField(("City"), max_length=20, choices=CITY_CHOICES, default='select')
    sdob = models.DateField(("DOB"), null=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(("Gender"), max_length=1, choices=GENDER_CHOICES, default='')


    class Meta:
        db_table = "student"

    def __str__(self):
        return self.sname


class Revenue(models.Model):
    MonthlyRevenue = models.CharField(max_length=50)
    Month = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.MonthlyRevenue, self.Month)

    
