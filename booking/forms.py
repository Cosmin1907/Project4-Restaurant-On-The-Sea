from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'phone_number', 'user', 'date', 'time_slot', 'no_of_guests', 'booking_notes')