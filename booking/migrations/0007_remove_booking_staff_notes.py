# Generated by Django 4.2.13 on 2024-07-04 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_table_table_notes_booking_staff_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='staff_notes',
        ),
    ]
