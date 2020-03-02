from django.contrib import admin
from django.urls import path
from . import views
from photos.views import HomeView, DetailView, CreateView

urlpatterns = [
    path('', HomeView.as_view(), name='photos_home'),
    path('photos/(?P<pk>[0-9]+)', DetailView.as_view(), name='photo_detail'),
    path('photos/new_photo', CreateView.as_view(), name='create_photo')
]