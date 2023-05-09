from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='offers-index'),
    path('cart', views.add_offer_to_cart, name='add_offer_to_cart'),
    path('<int:id>/', views.get_offer_by_id, name="offer-details"),  # Updated pattern
]
