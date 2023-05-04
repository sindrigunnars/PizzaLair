from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='userprofile-index'),
    path('register/', views.register, name='register'),
]