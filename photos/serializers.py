from rest_framework import serializers
from photos.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        read_only_fields = ('owner',) #Adjudica a solo lectura el campo 'owner' para el serializer
        exclude = []

class PhotoListSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')
