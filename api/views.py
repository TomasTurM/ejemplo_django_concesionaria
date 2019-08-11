from django.shortcuts import render

from rest_framework import generics
from concesionaria import models
from . import serializers

# Create your views here.

class ListAuto(generics.ListCreateAPIView):
    queryset = models.Auto.objects.all()
    serializer_class = serializers.AutoSerializer

class DetailAuto(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Auto.objects.all()
    serializer_class = serializers.AutoSerializer
