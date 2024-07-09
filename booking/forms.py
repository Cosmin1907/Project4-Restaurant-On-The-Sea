import random
from .models import Booking, Table
from django import forms
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'phone_number', 'date', 'time_slot', 'no_of_guests', 'booking_notes')
        # Source: https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
        }
        help_texts = {
            'name': 'Enter your full name.',
            'phone_number': 'Enter your phone number in the format: +123456789.',
            'date': 'Select the booking date. Date cannot be in the past.',
            'time_slot': 'Select a time slot for your booking. Start time must be in the future',
            'no_of_guests': 'Enter the number of guests.',
            'booking_notes': 'Any additional information or requests.',
        }

    #Code inspired and adapted from, source: https://docs.djangoproject.com/en/5.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time_slot = cleaned_data.get("time_slot")

        if date and date < timezone.now().date():
            self.add_error('date', ValidationError("The date cannot be in the past."))
        
        if date == timezone.now().date():
            start_times = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00"]
            selected_time = start_times[time_slot - 1]
            current_time = timezone.now().time()

            #Source: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
            if current_time >= datetime.strptime(selected_time, "%H:%M").time():
                self.add_error('time_slot', "The selected time slot has already passed for today.")

    def save(self, commit=True):
        # Get an unsaved instance of the model
        booking = super().save(commit=False)
        guests = booking.no_of_guests
        
        # Create a table with the required capacity
        if guests <= 2:
            capacity = 2
            table_limit = 4
            table_number = random.randint(1, 4)
        elif guests <= 4:
            capacity = 4
            table_limit = 4
            table_number = random.randint(5, 8)
        elif guests <= 6:
            capacity = 6
            table_limit = 2
            table_number = random.randint(9, 10)

        # Filter existing bookings for the given date and time slot and capacity
        no_of_tables = Booking.objects.filter(date=booking.date, time_slot=booking.time_slot, booked_table__capacity=capacity).count()

        if not booking.booked_table:
            if no_of_tables >= table_limit:
                raise ValidationError(f"No tables available for capacity in this interval")

            table = Table.objects.create(table_number=table_number, capacity=capacity)
            booking.booked_table = table

        # Save the instance only if commit is True
        if commit:
            booking.save()
        return booking