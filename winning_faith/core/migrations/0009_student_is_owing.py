# Generated by Django 5.0.6 on 2024-05-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_classroom_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_owing',
            field=models.BooleanField(default=True),
        ),
    ]