from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
from common.permissions import IsAdminOrReadOnly

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]