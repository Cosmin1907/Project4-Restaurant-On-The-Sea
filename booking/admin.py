from django.contrib import admin
from .models import Table, Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'user', 'date', 'time_slot', 'no_of_guests', 'booking_notes']
    list_filter = ['date', 'time_slot']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'table_notes']

