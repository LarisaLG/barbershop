# Generated by Django 3.2.16 on 2022-11-24 20:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Please enter a valid phone number, e.g. 123456789. Up to 15 digits allowed.', regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
