from django.urls import path
from photos.api import PhotoViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

# APIRouter
router = DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    # Photos API URLs
    path('1.0/', include(router.urls))  # Incluyo las urls de API
]