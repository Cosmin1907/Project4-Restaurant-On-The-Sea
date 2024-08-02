from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:post_id>/<int:rating>/', views.rate, name='rate'),
    path('rating/', views.index, name='ratings'),
]
