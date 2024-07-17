from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import BookingForm
from .models import Booking
from django.test import Client


# Create your tests here.
# Part of the coude inspired by Source: 
# https://docs.djangoproject.com/en/5.0/topics/testing/tools/#the-test-client

class TestBookingViews(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create a superuser
        self.superuser = User.objects.create_superuser(
            username="admin",
            password="adminPass",
            email="admin@test.com"
        )

        # Create regular user
        self.regular_user = User.objects.create_user(
            username="user",
            password="userPass",
            email="user@test.com"
        )

        # Create bookings for each user
        self.booking1 = Booking.objects.create(
            name="Admin",
            user=self.superuser,
            phone_number="+40723974593",
            date=date.today() + timedelta(days=1),  
            time_slot=1,
            no_of_guests=1
        )

        self.booking2 = Booking.objects.create(
            name="User",
            user=self.regular_user,
            phone_number="+40723974587",
            date=date.today() + timedelta(days=1),  
            time_slot=2,
            no_of_guests=2
        )


        