from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='menu-index'),
    # path('', views.search, name='search'),
    # path('', views.order_by, name='order-by'),
    path('<int:id>', views.get_pizza_by_id, name="pizza-details")
]