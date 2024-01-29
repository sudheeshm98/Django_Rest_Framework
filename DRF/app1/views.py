from django.shortcuts import render
from rest_framework.response import Response

from .models import Register
from .serializers import RegisterSerializer
from rest_framework import generics

# Create your views here.

class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data)

