
from photos.serializers import PhotoSerializer
from photos.models import Photo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
