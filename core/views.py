from django.shortcuts import render, get_object_or_404, redirect
from django.core import exceptions
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import MyUser, MyUserSerializerGET, MyUserSerializerPOST, MyUserSerializerPUT

# Create your views here.


class APIListUserView(APIView):

    def get(self, request, format = None):
        user = MyUser.objects.all()
        user_serializer = MyUserSerializerGET(user, many = True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format = None):
        user_serializer = MyUserSerializerPOST(data=self.request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()

            token, created = Token.objects.get_or_create(user=user)

            response_data = {
                'user': MyUserSerializerGET(user).data,
                'token':token.key
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({'message':'Los datos del formulario no estan en el formato correcto'}, status=status.HTTP_400_BAD_REQUEST)
    
