from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Booking
from .forms import BookingForm


# Create your views here.
class BookingList(generic.ListView):
    model = Booking
    template_name = "booking/booking_list.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

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
            #The code was adapted to the requirements, Source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
            try:
                booking = form.save(commit=False)
                booking.user = request.user  # Set the user field to the currently logged-in user
                booking.save()
                messages.success(self.request, "Booking successfully created!")
                return redirect("booking-list")
            except ValidationError as e:
                form.add_error(None, e)
        return render(request, "booking/booking_table.html", {'form': form})

#Source: https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#updateview
class BookingUpdate(UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_table.html"
    success_url = "/booking/list"

    def form_valid(self, form):
        messages.success(self.request, 'Booking Updated!')
        return super().form_valid(form)

    def test_func(self):
        """ Test user is staff else throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user


#Source: https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#deleteview
class BookingDelete(UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    success_url = reverse_lazy("booking-list")

    def form_valid(self, form):
        messages.success(self.request, 'Booking Deleted!')
        return super().form_valid(form)

    def test_func(self):
        """ Test user is staff else throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user


def custom_403(request, exception):
    return render(request, '403.html', status=403)




