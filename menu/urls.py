from django.urls import path
from menu.views import MenuPage

urlpatterns = [
    path('', MenuPage.as_view(), name='menu'),
]
