from django.contrib import admin
from .models import Booking, Table

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin view for Booking model.

    Allows filtering by:
    - date
    - time_slot
    """
    list_display = ['name', 'phone_number', 'user', 'date', 'time_slot', 'no_of_guests', 'booked_table', 'booking_notes']
    list_filter = ['date', 'time_slot']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin view for Table model.
    """
    list_display = ['table_number', 'capacity']
