# Generated by Django 3.0.5 on 2020-06-11 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_citizendiseaserelation_historic_locations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CitizenLocationSync',
        ),
    ]
