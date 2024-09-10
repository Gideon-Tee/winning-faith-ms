from django import forms
from .models import Student, Classroom, Teacher


class EnrollStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['full_name', 'fees_rem', 'is_owing', 'id']
        widgets = {
            'date_enrolled': forms.DateInput(attrs={'class': 'form-control'})
        }

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ['id', 'num_of_students']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['id', 'full_name']

        