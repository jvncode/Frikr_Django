from django.contrib import admin
from django.urls import path
from . import views
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from photos.api import PhotoListAPI, PhotoDetailAPI
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name='photos_home'),
    path('my-photos/', login_required(UserPhotosView.as_view()), name='user_photos'),
    path('photos/', PhotoListView.as_view(), name='photos_list'),
    path('photos/(<pk>)', DetailView.as_view(), name='photo_detail'),
    path('photos/new_photo', CreateView.as_view(), name='create_photo'),

    # Photos API URLs
    path('api/1.0/photos/', PhotoListAPI.as_view(), name='photo_list_api'),
    path('api/1.0/photos/<pk>', PhotoDetailAPI.as_view(), name='photo_detail_api')
]