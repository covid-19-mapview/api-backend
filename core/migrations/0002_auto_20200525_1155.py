# Generated by Django 3.0.5 on 2020-05-25 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patienthistoriclocation',
            old_name='infection_status',
            new_name='disease_infection_status',
        ),
    ]
