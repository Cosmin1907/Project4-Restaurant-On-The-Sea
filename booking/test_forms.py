from django.test import TestCase
from .forms import BookingForm
from datetime import date, timedelta 

# Create your tests here.

class TestBookingForm(TestCase):
   
   def test_form_is_valid(self):
        form = BookingForm({
         'name': 'Name',
         'phone_number': '+40723974937',
         'date': (date.today() + timedelta(days=1)).isoformat(),  # Valid future date
         'time_slot': 1, 
         'no_of_guests': 1
        })
        self.assertTrue(form.is_valid())

   def test_name_is_required(self):
        form = BookingForm({
         'name': '',
         'phone_number': '+40723974937',
         'date': (date.today() + timedelta(days=1)).isoformat(), 
         'time_slot': 1, 
         'no_of_guests': 1
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )
        
   def test_phone_is_required(self):
        form = BookingForm({
         'name': 'Name',
         'phone_number': '',
         'date': (date.today() + timedelta(days=1)).isoformat(),  
         'time_slot': 1, 
         'no_of_guests': 1
        })
        self.assertFalse(
            form.is_valid(),
            msg="Phone Number was not provided, but the form is valid"
        )

   def test_date_is_required(self):
        form = BookingForm({
         'name': 'Name',
         'phone_number': '+40723974937',
         'date': '',
         'time_slot': 1, 
         'no_of_guests': 1
        })
        self.assertFalse(
            form.is_valid(),
            msg="Date was not provided, but the form is valid"
        )       

   def test_time_is_required(self):
        form = BookingForm({
         'name': 'Name',
         'phone_number': '',
         'date': (date.today() + timedelta(days=1)).isoformat(),  
         'time_slot': None, 
         'no_of_guests': 1
        })
        self.assertFalse(
            form.is_valid(),
            msg="Time Slot was not provided, but the form is valid"
        )

   def test_guests_is_required(self):
        form = BookingForm({
         'name': 'Name',
         'phone_number': '',
         'date': (date.today() + timedelta(days=1)).isoformat(),  
         'time_slot': 1, 
         'no_of_guests': None
        })
        self.assertFalse(
            form.is_valid(),
            msg="Number of guests was not provided, but the form is valid"
        )

   def test_past_date(self):
        form = BookingForm({
         'name': 'Name',
         'phone_number': '+40723974937',
         'date': (date.today() - timedelta(days=1)).isoformat(),
         'time_slot': 1, 
         'no_of_guests': 1
        })
        self.assertFalse(
            form.is_valid(),
            msg="Date is in the past, but the form is valid"
        ) 

