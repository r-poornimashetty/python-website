# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Job, Student

admin.site.register(Job)
admin.site.register(Student)

