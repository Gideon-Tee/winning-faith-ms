# Generated by Django 5.0.6 on 2024-05-14 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_feespaid_student_fees_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_enrolled',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
