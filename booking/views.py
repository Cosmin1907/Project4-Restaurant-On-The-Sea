from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Booking
from .forms import BookingForm

# Create your views here.
class BookingList(generic.ListView):
    model = Booking
    template_name = "booking/booking_list.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)


class BookingTable(TemplateView):
    template_name = "booking/booking_table.html"
