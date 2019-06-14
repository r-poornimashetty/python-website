from django import forms
from job.models import Student

# class ConatctForm(forms.Form):
#     # name = forms.CharField(lable='your name', max_length=100)
#     contact_name = forms.CharField(widget=forms.TextInput())
#     contact_email = forms.EmailField(widget=forms.TextInput())

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['sid', 'sname', 'semail', 'scontact', 'scity', 'gender']
        widgets = {'gender': forms.RadioSelect}







