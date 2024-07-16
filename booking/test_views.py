from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import BookingForm
from .models import Booking


# Create your tests here.

class TestBookingViews(TestCase):
    def setUp(self):
        # Create a superuser
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        # Log in the user
        self.client.login(username="myUsername", password="myPassword")

        # Create a booking instance
        self.booking = Booking.objects.create(
            name="Name",
            phone_number="+40723974593",
            date=date.today() + timedelta(days=1),  
            time_slot=1,
            no_of_guests=1
        )
        