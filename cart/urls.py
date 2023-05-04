from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='cart-index'),
    path('cart', views.order, name='cart-order'),
    path('create_contact', views.create_contact, name='create_contact'),
    path('create_payment', views.create_payment, name='create_payment')
]