import random
from .models import Booking, Table
from django import forms
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'phone_number', 'date', 'time_slot', 'no_of_guests', 'booking_notes')
        # Source: https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
        }

    def save(self, commit=True):
        # Get an unsaved instance of the model
        booking = super().save(commit=False)

        # Count existing tables for the given date and time slot
        existing_bookings = Booking.objects.filter(date=booking.date, time_slot=booking.time_slot).count()
        if existing_bookings >= 2:
            raise ValidationError("No tables available for this date and time")
        
        # Find or create a table with the required capacity
        if not booking.booked_table:
            table_number = random.randint(1, 2)
            table = Table.objects.create(table_number=table_number, capacity=booking.no_of_guests)
               
            booking.booked_table = table

        # Save the instance only if commit is True
        if commit:
            booking.save()
        return booking