from django.shortcuts import render, redirect
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

#Source: https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/
class BookingTable(View):
    def get(self, request):
        form = BookingForm()
        return render(request, "booking/booking_table.html", {'form': form})

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking-list")
        return render(request, 'booking/booking_table.html', {'form': form})
