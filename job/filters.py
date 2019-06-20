import django_filters
from job.models import Student
from .forms import StudentForm

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['sname', 'semail', 'scontact', ]
