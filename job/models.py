# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    sname = models.CharField(max_length=100)
    semail = models.EmailField()
    scontact = models.CharField(max_length=15)
    scity= models.CharField(max_length=6, choices=CITY_CHOICES, default='select')
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')


    class Meta:
        db_table = "student"

    def __str__(self):
        return self.sname

    
