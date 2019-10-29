from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import *


# Create your APIs here.
class listGym(generics.RetrieveUpdateAPIView):
    queryset = Gym.objects.all()
    serializer_class = gymAPI


# Create your views here.
