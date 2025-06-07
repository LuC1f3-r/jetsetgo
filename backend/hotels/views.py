from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer
from common.permissions import IsAdminOrReadOnly

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
