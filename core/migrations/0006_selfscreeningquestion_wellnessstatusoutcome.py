# Generated by Django 3.0.5 on 2020-06-03 02:44

import authentication.utils
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_riskassessmentrecommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfScreeningQuestion',
            fields=[
                ('id', models.CharField(default=authentication.utils.hex_uuid, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('instruction', models.TextField()),
                ('question', models.TextField()),
                ('choices', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='WellnessStatusOutcome',
            fields=[
                ('id', models.CharField(default=authentication.utils.hex_uuid, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('outcome', models.CharField(max_length=80)),
                ('point_upper_limit', models.FloatField()),
                ('point_lower_limit', models.FloatField()),
            ],
        ),
    ]
