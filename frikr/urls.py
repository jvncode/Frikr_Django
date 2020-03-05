
from django.contrib import admin
from django.urls import path, include
from photos import api_urls as photos_api_urls
from users import api_urls as users_api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # Photos URLs
    path('', include('photos.urls')),
    path('api/', include(photos_api_urls)),
    # Users URLs
    path('', include('users.urls')),
    path('api/', include(users_api_urls))
]
