from django.urls import path
from users.api import UserViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

# APIRouter
router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    # Users API URLs
    path('1.0/', include(router.urls))  # Incluyo las urls de API
]