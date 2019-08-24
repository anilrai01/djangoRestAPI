from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import parkingSpace
from .serializers import GridSerializer

class GridList(generics.ListAPIView):
    queryset = parkingSpace.objects.all()
    serializer_class = GridSerializer

class GridDetail(generics.RetrieveAPIView):
    queryset = parkingSpace.objects.all()
    serializer_class = GridSerializer

