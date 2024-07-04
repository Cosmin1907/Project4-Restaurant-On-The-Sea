from django.contrib import admin
from .models import Booking, Table

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'user', 'date', 'time_slot', 'no_of_guests', 'booked_table', 'booking_notes']
    list_filter = ['date', 'time_slot']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity']
