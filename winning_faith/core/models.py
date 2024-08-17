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

category_choices = (
    ('crech', 'Crech / Kindergarten'),
    ('lower_primary', 'Lower primary'),
    ('upper_primary', 'Upper primary'),
    ('jhs', 'JHS')
)



class Student(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    other_names = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length = 100, editable=False)
    guardian_full_name = models.CharField(max_length=255)
    guardian_phone_number = models.IntegerField()
    guardian_relation = models.CharField(max_length=25)
    fees_paid = models.FloatField()
    fees_rem = models.FloatField(default=0.0)
    is_owing = models.BooleanField(default=False)
    date_enrolled = models.DateField(default=datetime.now)
    classroom = models.ForeignKey('Classroom', to_field='name', on_delete=models.PROTECT)

    def calcRemainingFees(self) -> float:
        fee_required = fees.get(self.category, 0.0)
        fees_remaining = fee_required - float(self.fees_paid)
        print(f"Calculating remaining fees: fee_required={fee_required}, fees_paid={self.fees_paid}, remaining_fees={fees_remaining}")

        return fees_remaining 
    
    def isOwingFees(self) -> bool:
        # fee_required = 0.0
        fee_required = fees.get(self.category, 0.0)
        return float(self.fees_paid) < float(fee_required)
    
    def getFullName(self) -> str:
        return f'{self.lname} {self.fname} {self.other_names}'

    def save(self, *args, **kwargs):
        self.is_owing = self.isOwingFees()
        self.fees_rem = self.calcRemainingFees()
        self.full_name = self.getFullName()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
class Classroom(models.Model):
    name = models.CharField(max_length=25, unique=True)
    num_of_students = models.IntegerField(blank = True, default=0)
    category = models.CharField(max_length=25, choices=category_choices)
    # class_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL)
    

    def __str__(self):
        return f'{self.name}'
    
class Teacher(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    other_names = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=100, editable=False)
    assigned_class = models.OneToOneField(Classroom, on_delete=models.SET_NULL, related_name='class_teacher', to_field='name', null=True, blank=True)


    def getFullName(self):
        return f'{self.lname} {self.fname} {self.other_names}'

    def save(self, *args, **kwargs):
        self.full_name = self.getFullName()
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.fname} {self.lname}'


class Fee:
    crech: float
    lower_primary: float
    upper_primary: float
    jhs: float