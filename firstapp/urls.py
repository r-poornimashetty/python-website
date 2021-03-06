"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import job.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url('signup/', job.views.signup, name='signup'),
    url('home/', job.views.home, name='home'),
    url('about/', job.views.about, name='about'),
    url('contact/', job.views.contact, name='contact'),
    url('studentform/', job.views.std, name='studentform'),
    url('student/add', job.views.StudentCreateView.as_view(), name='student-add'),
    url('student/list', job.views.StudentListView.as_view(), name='student-add'),
    url('student/edit/(?P<pk>\d+)', job.views.StudentUpdate.as_view(), name='student-add'),
    url('studentdetails/', job.views.studentdetails, name='studentdetails'),
    url('studentedit/(?P<id>\d+)', job.views.studentedit, name='studentedit'),
    url('updatestudent/(?P<id>\d+)', job.views.updatestudent, name='updatestudent'),
    url('delete/(?P<id>\d+)', job.views.destroy, name='delete'),

    # url('student/', include('student.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
