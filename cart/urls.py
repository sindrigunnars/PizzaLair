from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='cart-index'),
    path('cart', views.order, name='cart-order')
]