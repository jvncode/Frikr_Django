from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='photos_home'),
    path('photos/<pk>', views.detail, name='photo_detail')

]