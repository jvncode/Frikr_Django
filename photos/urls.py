from django.urls import path
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url

urlpatterns = [
    path('', HomeView.as_view(), name='photos_home'),
    path('my-photos/', login_required(UserPhotosView.as_view()), name='user_photos'),
    path('photos/', PhotoListView.as_view(), name='photos_list'),
    path('photos/(<pk>)', DetailView.as_view(), name='photo_detail'),
    path('photos/new_photo', CreateView.as_view(), name='create_photo'),
]