# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.core.validators import MinLengthValidator
import datetime
from job.tasks import set_race_as_inactive

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

class College(models.Model):
    collegename = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.collegename

class DegreeStream(models.Model):
    dstream = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.dstream

class DiplomaStream(models.Model):
    diplomastream = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.diplomastream

class MasterDegreeStream(models.Model):
    masterdegreestream = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.masterdegreestream

STATE_CHOICES=[
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal')
]

twelthboard_CHOICES=[
    ('None', 'None'),
    ('Puc/12th', 'Puc/12th'),
    ('Diploma', 'Diploma'),
    ('ITI', 'ITI')
] 

Degree_CHOICES=[
    ('-none-', '-none-'),
    ('BE', 'BE'),
    ('BSC', 'BSC'),
    ('BCA', 'BCA'),
    ('BECOM', 'BECOM'),
    ('BTECH', 'BETEC'),
    ('BBM', 'BBM'),
    ('BA', 'BA')
]

Master_Degree_CHOICES=[
    ('-none-', '-none-'),
    ('M.Tech', 'M.Tech'),
    ('M.E', 'M.E'),
    ('MSC', 'MSC'),
    ('MCA', 'MCA'),
    ('MBA', 'MBA'),
    ('MPhil', 'MPhil'),
    ('MA', 'MA'),
    ('MSW', 'MSW'),
    ('MHM', 'MHM'),
    ('MCOM', 'MCOM'),
    ('Other', 'Other')
]

year_choices= [(r,r) for r in range(1984, datetime.datetime.today().year+1)]

def current_year():
    return datetime.datetime.today().year

class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(("First Name"), max_length=100)
    lastname = models.CharField(("Last Name"), max_length=20,  null=True)
    semail = models.EmailField(("Email"))
    scontact = models.CharField(("Contact"), max_length=15)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(("Gender"), max_length=15, choices=GENDER_CHOICES, default='')
    country = CountryField(("Country"),blank_label='(select country)', null=True)
    sate= models.CharField(("State"), max_length=20, choices=STATE_CHOICES, default='select')
    scity= models.CharField(("City"), max_length=20, default='')
    pincode= models.IntegerField(("Pincode"), null=True)
    sdob = models.DateField(("DOB"), null=True)
    twelthboard= models.CharField(("12th board"), max_length=20, choices=twelthboard_CHOICES, default='none')
    Diploma_Stream = models.ForeignKey(DiplomaStream, on_delete=models.SET_NULL, null=True)
    puc_diploma_year = models.IntegerField(('YOP'), choices=year_choices, default=current_year, null=True)
    degree = models.CharField(("Degree"), max_length=20, choices=Degree_CHOICES, default='none')
    Degree_College = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, related_name='Degree_College')
    degree_Stream = models.ForeignKey(DegreeStream, on_delete=models.SET_NULL, null=True)
    Degree_year = models.IntegerField(('YOP'), choices=year_choices, default=current_year, null=True)
    masterdegree_choices = (('Yes', 'Yes'), ('No', 'No'))
    masterdegreeoption = models.CharField(("Have you done Master Degree?"), max_length=10, choices=masterdegree_choices, default='')
    master_Degree = models.CharField(("Matser Degree"), max_length=20, choices=Master_Degree_CHOICES, default='none')
    Master_Degree_Stream = models.ForeignKey(MasterDegreeStream, on_delete=models.SET_NULL, null=True)
    Master_Degree_College = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, related_name='Master_Degree_College')
    Master_Degree_year = models.IntegerField(('YOP'), choices=year_choices, default=current_year, null=True)

    


    class Meta:
        db_table = "student"

    def __str__(self):
        return self.sname



class Revenue(models.Model):
    MonthlyRevenue = models.CharField(max_length=50)
    Month = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.MonthlyRevenue, self.Month)


class AddProject(models.Model):
    project_name = models.CharField(max_length=100)
    start_date = models.DateField(("Start Date"), null=True)
    end_date = models.DateField(("End Date"), null=True)

    def save(self, *args, **kwargs):
        create_task = False
        if self.pk is None: 
            create_task = True # set the variable 

        super(AddProject, self).save(*args, **kwargs) 

        if create_task: 
            set_race_as_inactive.apply_async(args=[self], eta=self.end_date) 

    
