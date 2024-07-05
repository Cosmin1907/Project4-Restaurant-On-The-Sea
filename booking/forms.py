from .models import Booking, Table
from django import forms

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
        
        # Find or create a table with the required capacity
        if not booking.booked_table:
            table = Table.objects.filter(capacity=booking.no_of_guests, booking__isnull=True).first()
            if not table:
                table_number = Table.objects.count() + 1  # Assign the next table number
                table = Table.objects.create(table_number=table_number, capacity=booking.no_of_guests)
            booking.booked_table = table

        # Save the instance only if commit is True
        if commit:
            booking.save()
        return booking