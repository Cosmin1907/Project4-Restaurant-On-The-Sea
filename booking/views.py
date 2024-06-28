from django.shortcuts import render
from django.views import generic, View
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


class BookingTable(View):
    def get(self, request):
        form = BookingForm()
        return render(request, 'booking/booking_table.html', {'form': form})
