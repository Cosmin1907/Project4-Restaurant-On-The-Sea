from . import views
from django.urls import path
from .views import BookingList, BookingTable, BookingUpdate, BookingDelete

urlpatterns = [
    path('list/', views.BookingList.as_view(), name='booking-list'),
    path('table/', views.BookingTable.as_view(), name='booking-table'),
    path('booking/edit/<int:pk>/', BookingUpdate.as_view(), name='booking-update'),
    path('booking/delete/<int:pk>/', BookingDelete.as_view(), name='booking-delete'),
]