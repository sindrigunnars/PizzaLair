from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='Home Page'),
    path('about_us/', views.about_us, name='About Us'),
    path('locations/', views.locations, name='Locations'),
    path('contact_us/', views.contact_us, name='Contact Us'),
]
