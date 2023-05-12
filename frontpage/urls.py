from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='frontpage-index'),
    path('about_us', views.about_us, name='about_us'),
    path('locations', views.locations, name='locations'),
    path('contact_us', views.contact_us, name='contact_us')
]
