# Generated by Django 4.2.13 on 2024-08-07 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+<country code><number>'or '00<country code><number>'. Up to 15 digits allowed, with a minimum of 10 digits required.", regex='^(?:\\+|00)[1-9]\\d{9,14}$')]),
        ),
    ]