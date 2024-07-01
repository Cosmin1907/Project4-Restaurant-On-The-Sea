from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'phone_number', 'date', 'time_slot', 'no_of_guests', 'booking_notes')
        # Source: https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
        }