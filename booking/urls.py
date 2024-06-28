from . import views
from django.urls import path
from .views import BookingList, BookingTable

urlpatterns = [
    path('list/', views.BookingList.as_view(), name='booking-list'),
    path('table/', views.BookingTable.as_view(), name='booking-table'),
]