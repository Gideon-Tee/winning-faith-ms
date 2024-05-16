from django.db import models
import uuid
from datetime import datetime
# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    other_names = models.CharField(max_length=100, blank=True)
    fees_paid = models.FloatField()
    date_enrolled = models.DateField(default=datetime.now)
    classroom = models.CharField(max_length=25)
    category = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=25)
    num_of_students = models.IntegerField(blank = True, default=0)
    class_teacher = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    other_names = models.CharField(max_length=100, blank=True)
    assigned_class = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fname} {self.lname}'
