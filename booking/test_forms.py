from datetime import date, timedelta
from django.test import TestCase
from freezegun import freeze_time
from .forms import BookingForm


# Create your tests here.
class TestBookingForm(TestCase):
    """
    Test cases for BookingForm.
    """

    def test_form_is_valid(self):
        """
        Test that the form is valid with correct input.
        """
        form = BookingForm({
            'name': 'Name',
            'phone_number': '+40723974937',
            # Valid future date
            'date': (date.today() + timedelta(days=1)).isoformat(),
            'time_slot': 1,
            'no_of_guests': 1
        })
        self.assertTrue(form.is_valid())

    def test_name_is_required(self):
        """
        Test that the name field is required.
        """
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
        """
        Test that the phone number field is required.
        """
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
        """
        Test that the date field is required.
        """
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
        """
        Test that the time slot field is required.
        """
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
        """
        Test that the number of guests field is required.
        """
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
        """
        Test that the date cannot be in the past.
        """
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

# Code inspired by Source: https://github.com/spulec/freezegun
    @freeze_time(lambda: date.today().isoformat() + " 10:30:00")
    def test_time_slot_is_in_past(self):
        """
        Test that the time slot cannot be in the past for today's date.
        """
        form = BookingForm({
            'name': 'Name',
            'phone_number': '+40723974937',
            'date': date.today().isoformat(),  # Today's date
            'time_slot': 1,  # 1 corresponds to "09:00 - 10:45"
            'no_of_guests': 1
        })
        self.assertFalse(
            form.is_valid(),
            msg="The time slot is in the past, but the form is valid"
        )

    def test_wrong_phone_format(self):
        """
        Test that the phone number format is validated.
        """
        form = BookingForm({
            'name': 'Name',
            'phone_number': '7239749373',
            'date': (date.today() + timedelta(days=1)).isoformat(),
            'time_slot': 1,
            'no_of_guests': 1
        })

        self.assertFalse(
            form.is_valid(),
            msg="The phone format is incorect, but the form is valid"
        )
