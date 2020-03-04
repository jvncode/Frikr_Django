
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.models import Photo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from photos.views import PhotosQueryset

class PhotoListAPI(PhotosQueryset, ListCreateAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer
    
    def get_queryset(self):
        return self.get_photos_queryset(self.request)
    
    def perform_create(self, serializer):  #Se encarga de limitar al usuario autenticado la creación desde la API
        serializer.save(owner=self.request.user)


class PhotoDetailAPI(PhotosQueryset, RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)
