from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
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
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user field to the currently logged-in user
            booking.save()
            return redirect("booking-list")
        return render(request, "booking/booking_table.html", {'form': form})

#Source: https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#updateview
class BookingUpdate(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_table.html"
    success_url = "/booking/list"

