# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Student

# Create your views here.
def student(request):
    students = Student.objects
    return render(request, 'student/student.html', {'students':students})
