from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='users_login'),
    path('logout', views.logout, name='users_logout')
]