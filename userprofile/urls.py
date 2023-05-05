from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='userprofile-index'),
    path('register/', views.register, name='register'),
    path('login', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile')
]