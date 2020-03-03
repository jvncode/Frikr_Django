from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status

class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)  #many es necesario para cuando pasas más de un objeto
        serialized_users = serializer.data  #lista de diccionarios
        return Response(serialized_users)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user) #UserSerializer devuelve un diccionario en serializer.data
        return Response(serializer.data)


