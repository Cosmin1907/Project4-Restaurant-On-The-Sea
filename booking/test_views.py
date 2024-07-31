from datetime import date, timedelta
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.test import TestCase
from .forms import BookingForm
from .models import Booking


# Create your tests here.
# Part of the code inspired by Source:
# https://docs.djangoproject.com/en/5.0/topics/testing/tools/#the-test-client
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises

class TestBookingViews(TestCase):
    """
    Test case for booking-related views.
    """
    def setUp(self):
        """
        Set up test environment with sample users and bookings.
        """
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

        # Create bookings using the form to ensure all logic is executed
        booking_data1 = {
            'name': 'Admin Booking',
            'user': self.superuser,
            'phone_number': '+40723974593',
            'date': date.today() + timedelta(days=1),
            'time_slot': 1,
            'no_of_guests': 1,
        }
        form1 = BookingForm(data=booking_data1)
        if form1.is_valid():
            self.booking1 = form1.save(commit=False)
            self.booking1.user = self.superuser
            self.booking1.save()

        booking_data2 = {
            'name': 'User Booking',
            'user': self.regular_user,
            'phone_number': '+40723974587',
            'date': date.today() + timedelta(days=1),
            'time_slot': 2,
            'no_of_guests': 2,
        }
        form2 = BookingForm(data=booking_data2)
        if form2.is_valid():
            self.booking2 = form2.save(commit=False)
            self.booking2.user = self.regular_user
            self.booking2.save()

    def test_booking_list_view(self):
        """
        Test booking list view for different user types.
        """
        # Log in as superuser and test
        self.client.login(username="admin", password="adminPass")
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_list.html')
        self.assertContains(response, 'Made by: Admin Booking')
        self.assertContains(response, 'Made by: User Booking')
        self.assertContains(response, 'Capacity: 2')

        # Log in as regular user and test
        self.client.login(username='user', password='userPass')
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_list.html')
        self.assertContains(response, 'Made by: User Booking')
        self.assertNotContains(response, 'Made by: Admin Booking')
        self.assertNotContains(response, 'Capacity: 2')

    def test_booking_table_view(self):
        """
        Test booking creation.
        """
        self.client.login(username='user', password='userPass')
        response = self.client.post(reverse('booking-table'), {
            'name': 'New Booking',
            'phone_number': '+40723974595',
            'date': date.today() + timedelta(days=2),
            'time_slot': 3,
            'no_of_guests': 3,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(name='New Booking').exists())

    def test_user_update_booking(self):
        """
        Test booking update by a regular user.
        """
        self.client.login(username='user', password='userPass')
        response = self.client.post(
            reverse('booking-update', kwargs={'pk': self.booking2.pk}),
            {
                'name': 'Updated by User',
                'phone_number': '+40723974594',
                'date': date.today() + timedelta(days=4),
                'time_slot': 4,
                'no_of_guests': 4,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.booking2.refresh_from_db()
        self.assertEqual(self.booking2.name, 'Updated by User')
        self.assertEqual(self.booking2.booked_table.capacity, 4)

    def test_superuser_update_booking(self):
        """
        Test booking update by a superuser.
        """
        self.client.login(username='admin', password='adminPass')
        response = self.client.post(
            reverse('booking-update', kwargs={'pk': self.booking2.pk}),
            {
                'name': 'Updated Booking by Admin',
                'phone_number': '+40723974594',
                'date': date.today() + timedelta(days=4),
                'time_slot': 5,
                'no_of_guests': 5,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.booking2.refresh_from_db()
        self.assertEqual(self.booking2.name, 'Updated Booking by Admin')
        self.assertEqual(self.booking2.booked_table.capacity, 6)

    def test_regular_user_delete_booking(self):
        """
        Test booking deletion by a regular user.
        """
        self.client.login(username='user', password='userPass')
        response = self.client.post(
            reverse(
                'booking-delete',
                kwargs={
                    'pk': self.booking2.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(pk=self.booking2.pk)

    def test_superuser_delete_booking(self):
        """
        Test booking deletion by a superuser.
        """
        # Superuser can delete any booking
        self.client.login(username='admin', password='adminPass')
        response = self.client.post(
            reverse(
                'booking-delete',
                kwargs={
                    'pk': self.booking2.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(pk=self.booking2.pk)

        self.client.login(username='admin', password='adminPass')
        response = self.client.post(
            reverse(
                'booking-delete',
                kwargs={
                    'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(pk=self.booking1.pk)

    def test_custom_403_page(self):
        """
        Test custom 403 error page for unauthorized actions.
        """
        self.client.login(username='user', password='userPass')
        response = self.client.get(
            reverse(
                'booking-update',
                kwargs={
                    'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')
