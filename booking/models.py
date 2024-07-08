from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Phone number validator
# Source: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
phone_validator = RegexValidator(
    regex=r'^\+?[1-9]\d{0,3}\d{4,14}$',
    message="Phone number must be entered in the format: '<country code><local number>'. Up to 15 digits allowed, with an optional leading '+'."
)

# Time slots for booking
TIME_SLOTS = (
    (1, "09:30 - 11:00"),
    (2, "11:30 - 13:00"),
    (3, "13:30 - 15:00"),
    (4, "15:30 - 17:00"),
    (5, "17:30 - 19:00"),
    (6, "19:30 - 21:00"),
)

GUESTS = (
    (1, "1 guest"),
    (2, "2 guests"),
    (3, "3 guests"),
    (4, "4 guests"),
    (5, "5 guests"),
    (6, "6 guests"),
)

# Create your models here.
class Table(models.Model):
    table_number = models.PositiveIntegerField()
    capacity = models.IntegerField()
    
    class Meta:
        ordering = ["table_number"] 

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


class Booking(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(validators=[phone_validator], max_length=17)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    no_of_guests = models.IntegerField(choices=GUESTS)
    date = models.DateField()
    time_slot = models.IntegerField(choices=TIME_SLOTS) 
    booked_table = models.ForeignKey(Table, on_delete=models.CASCADE, blank=True, null=True) 
    booking_notes = models.TextField(blank=True) # Field for customer notes

    class Meta:
        ordering = ["date", "time_slot"]

    def __str__(self):
        return f"Booking for {self.no_of_guests} on {self.date} booked by {self.name}"

