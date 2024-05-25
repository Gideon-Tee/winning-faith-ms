from django.db import models
import uuid
from datetime import datetime
# Create your models here.


fees = {
    'crech': 500.0,
    'lower_primary': 650.0,
    'upper_primary': 800.0,
    'jhs': 1000.0
}

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    other_names = models.CharField(max_length=100, blank=True)
    fees_paid = models.FloatField()
    fees_rem = models.FloatField(default=0.0)
    is_owing = models.BooleanField(default=False)
    date_enrolled = models.DateField(default=datetime.now)
    classroom = models.CharField(max_length=25)
    category = models.CharField(max_length=25)

    def calcRemainingFees(self):
        fee_required = fees.get(self.category, 0.0)
        fees_remaining = fee_required - self.fees_paid
        print(f"Calculating remaining fees: fee_required={fee_required}, fees_paid={self.fees_paid}, remaining_fees={fees_remaining}")

        return fees_remaining 
    
    def isOwingFees(self):
        # fee_required = 0.0
        fee_required = fees.get(self.category, 0.0)
        return self.fees_paid < fee_required

    def save(self, *args, **kwargs):
        self.is_owing = self.isOwingFees()
        self.fees_rem = self.calcRemainingFees()
        print(f'Before saving, fees remaining is {self.fees_rem}')
        super().save(*args, **kwargs)
        print(f'After saving, fees remaining is {self.fees_rem}')

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=25)
    num_of_students = models.IntegerField(blank = True, default=0)
    class_teacher = models.CharField(max_length=100)
    category = models.CharField(max_length=30, default = 'None')

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


class Fee:
    crech: float
    lower_primary: float
    upper_primary: float
    jhs: float