# Generated by Django 5.0.6 on 2024-05-14 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='feesPaid',
            new_name='fees_paid',
        ),
    ]
