from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from users.permissions import UserPermission
from rest_framework.viewsets import ViewSet


class UserViewSet(ViewSet):

    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (UserPermission,) # Agrega la nuestra clase creada a los permisos de restframework

    def list(self, request):
        self.check_permissions(request)
        paginator = PageNumberPagination()  #instanciar paginador
        users = User.objects.all() # En users estará el queryset, no los objetos
        paginator.paginate_queryset(users, request) #paginar el queryset
        serializer = UserSerializer(users, many=True)  #many es necesario para cuando pasas más de un objeto
        serialized_users = serializer.data  #lista de diccionarios
        #devolver respuesta paginada
        return paginator.get_paginated_response(serialized_users)

    def create(self, request):
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user) #UserSerializer devuelve un diccionario en serializer.data
        return Response(serializer.data)
    
    def update(self, request, pk):
        self.check_permissions(request) # Comprueba si el usuario puede hacer la acción
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user) # Comprueba si el usuario puede hacer la acción sobre el objeto que ha elegido
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

"""
A continuación el mismo código pero con sistema de Clases View:
class UserListAPI(APIView):

    permission_classes = (UserPermission,) # Agrega la nuestra clase creada a los permisos de restframework

    def get(self, request):
        self.check_permissions(request)
        paginator = PageNumberPagination()  #instanciar paginador
        users = User.objects.all() # En users estará el queryset, no los objetos
        paginator.paginate_queryset(users, request) #paginar el queryset
        serializer = UserSerializer(users, many=True)  #many es necesario para cuando pasas más de un objeto
        serialized_users = serializer.data  #lista de diccionarios
        #devolver respuesta paginada
        return paginator.get_paginated_response(serialized_users)

    def post(self, request):
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    permission_classes = (UserPermission,) # Agrega la nuestra clase creada a los permisos de restframework

    def get(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user) #UserSerializer devuelve un diccionario en serializer.data
        return Response(serializer.data)
    
    def put(self, request, pk):
        self.check_permissions(request) # Comprueba si el usuario puede hacer la acción
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user) # Comprueba si el usuario puede hacer la acción sobre el objeto que ha elegido
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""



