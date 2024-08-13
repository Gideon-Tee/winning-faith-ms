from django import forms
from django.forms import ModelForm
from .models import Student


class EnrollStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'fname', 'lname', 'other_names' \
            'fees_paid', 'date_enrolled', 'category'
        ]