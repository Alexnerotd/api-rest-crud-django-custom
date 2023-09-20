from django.shortcuts import render, get_object_or_404, redirect
from django.core import exceptions
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MyUser, MyUserSerializerGET, MyUserSerializerPOST, MyUserSerializerPUT

# Create your views here.


class APIListUserView(APIView):

    def get(self, request, format = None):
        user = MyUser.objects.all()
        user_serializer = MyUserSerializerGET(user, many = True)
        try:
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message':"La pagina a la que se esta intentando acceder no existe"})
        
    def post(self, request, format = None):
        user_serializer = MyUserSerializerPOST(data=self.request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'Los datos del formulario no estan en el formato correcto'}, status=status.HTTP_400_BAD_REQUEST)
    
