from django import forms
from .models import Student, Classroom


class EnrollStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['full_name', 'fees_rem', 'is_owing', 'id']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ['id', 'num_of_students']