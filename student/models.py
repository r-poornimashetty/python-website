# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=200)
    DOB = models.DateTimeField()
    
    def __unicode__(self):
        return self.Name
