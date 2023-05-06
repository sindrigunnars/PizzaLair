from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='menu-index'),
    path('<int:id>', views.get_pizza_by_id, name="pizza-details"),
    path('cart/', views.add_menu_to_cart, name='add_menu_to_cart')
]