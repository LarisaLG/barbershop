from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services/', views.services, name="services"),
    path('booknow/', views.booknow, name="booknow"),
    path('bookings/', views.bookings, name='bookings'),
]
