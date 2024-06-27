# Generated by Django 4.2.13 on 2024-06-21 13:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='notes',
            new_name='table_notes',
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '<country code><local number>'. Up to 15 digits allowed, with an optional leading '+'.", regex='^\\+?[1-9]\\d{0,3}\\d{4,14}$')])),
                ('no_of_guests', models.IntegerField()),
                ('date', models.DateField()),
                ('time_slot', models.IntegerField(choices=[(0, '09:30 - 11:00'), (1, '11:30 - 13:00'), (2, '13:30 - 15:00'), (3, '15:30 - 17:00'), (4, '17:30 - 19:00'), (5, '19:30 - 21:00')])),
                ('booking_notes', models.TextField(blank=True)),
                ('booked_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]