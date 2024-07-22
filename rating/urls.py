from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/<int:post_id>/<int:rating>/', views.rate),
    path('', views.index),
]