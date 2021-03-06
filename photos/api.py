
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.models import Photo
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from photos.views import PhotosQueryset
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

"""
Este ViewSet hace lo mismo que las clases PhotoListAPI y PhotoDetailAPI
pero en una sola clase
"""

class PhotoViewSet(PhotosQueryset, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter) # Esta linea, la 18 y 19, establecen metodos de búsqueda y orden de las entradas desde la API
    search_fields = ('name', 'description') # Esta por 'search' (búsqueda)
    ordering_fields = ('name', 'owner') # Esta por 'ordering' (orden)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto
        al usuario autenticado
        """
        serializer.save(owner=self.request.user)

"""
A continuación el mismo código pero en sistema de Clases View:

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
"""