from django.contrib import admin
from django.urls import path

from .views import register,user_login,user_profile,user_logout



urlpatterns = [
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('profile', user_profile, name='profile'),
    path('logout', user_logout, name='logout'),
    # path('login', LoginView.as_view(), name='login'),
    # path('logout', LogoutView.as_view(), name='logout'),
]