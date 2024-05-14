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
    date_enrolled = models.DateTimeField(default=datetime.now)
    classroom = models.CharField(max_length=25)
    category = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
