# Generated by Django 5.0.6 on 2024-05-25 15:59

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_student_is_owing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='is_owing',
            field=models.BooleanField(default=core.models.Student.isOwingFees),
        ),
    ]