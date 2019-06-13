# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages
from .models import Job, Student
from .forms import ContactForm, StudentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import UserFilter

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
    


def about(request): 
    return render(request, 'jobs/about-us.html')


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('jobs/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)  

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['r.poornimashetty@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Form submission successful')
            return redirect('contact')
    return render(request, 'jobs/contact.html', {
        'form': form_class,
    })



# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'jobs/signup.html', {'form': form})

def std(request):
    form = StudentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                return redirect('studentdetails')
            except: 
                pass
        else:
            form = StudentForm()
    return render(request, 'jobs/studentform.html', {'form':form})   

def studentdetails(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page', 1)

    
    try:
        Students = paginator.page(page)
    except PageNotAnInteger:
        Students = paginator.page(1)
    except EmptyPage:
        Students = paginator.page(paginator.num_pages)
    
    filter = UserFilter(request.GET, queryset= Students)
    return render(request, 'jobs/student_details.html', {'Students':Students, 'filter': filter})

def studentedit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'jobs/edit_student.html', {'student':student})

def updatestudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/studentdetails")  
    return render(request, 'jobs/edit_student.html', {'student':student})

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/studentdetails")  


