from socket import fromshare
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        labels = {"first_name": "Name:", "last_name": "Surname:", "number": "Number"}