from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='photos_home'),
    path('photos/(?P<pk>[0-9]+)', views.detail, name='photo_detail'),
    path('photos/new_photo', views.create, name='create_photo')
]