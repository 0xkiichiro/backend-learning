from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("fullname", "number", "mobile", "email", "gender", "path")
        labels = {
            "fullname": "Full Name",
            "number": "Student Number",
        }

    def __int__(self, *args, **kwargs):
        super(StudentForm, self).__int__(*args, **kwargs)
        self.fields["path"].empty_label = "Select"
        self.fields["number"].required = False