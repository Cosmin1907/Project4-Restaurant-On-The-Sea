# Generated by Django 4.2.13 on 2024-07-17 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_booking_no_of_guests_alter_booking_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+<country code><number>' or '00<country code><number>'. Up to 15 digits allowed, with a minimum of 10 digits required.", regex='^(?:\\+|00)[1-9]\\d{9,14}$')]),
        ),
    ]