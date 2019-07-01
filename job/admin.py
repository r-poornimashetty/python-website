# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Job, Student, Revenue, College, DegreeStream, DiplomaStream, MasterDegreeStream, AddProject

admin.site.register(Job)
admin.site.register(Student)
admin.site.register(Revenue)
admin.site.register(College)
admin.site.register(DegreeStream)
admin.site.register(DiplomaStream)
admin.site.register(MasterDegreeStream)
admin.site.register(AddProject)




