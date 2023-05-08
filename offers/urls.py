from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='offers-index'),
    path('<int:id>', views.get_offer_by_id, name="offer-details"),
    path('<int:id>', views.get_pizza_by_id, name="pizza-details"),
    path('cart', views.add_offer_to_cart, name='add_offer_to_cart')
]