from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.
class BookingList(generic.ListView):
    model = Booking
    template_name = "booking_list.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
