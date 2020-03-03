from django.contrib import admin
from django.urls import path
from . import views
from users.views import LoginView, LogoutView
from users.api import UserListAPI, UserDetailAPI

urlpatterns = [
    path('login', LoginView.as_view(), name='users_login'),
    path('logout', LogoutView.as_view(), name='users_logout'),

    # Users API URLs
    path('api/1.0/users/', UserListAPI.as_view(), name='user_list_api'),
    path('api/1.0/users/<pk>', UserDetailAPI.as_view(), name='user_detail_api')
]