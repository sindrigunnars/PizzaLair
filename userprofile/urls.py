from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='userprofile-index'),
    path('register/', views.register, name='register'),
    path('', LoginView.as_view(template_name='userprofile/index.html'), name='userprofile-index'),
    path('logout/', LoginView.as_view(next_page='userprofile/index.html'), name='logout'),
]