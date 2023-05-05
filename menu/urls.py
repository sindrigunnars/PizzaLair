from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='menu-index'),
    path('search/', views.search, name='search'),
    path('<int:id>', views.get_pizza_by_id, name="pizza-details")
]