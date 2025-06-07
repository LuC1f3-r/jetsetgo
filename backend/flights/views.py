from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Flight
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FlightSerializer
from common.permissions import IsAdminOrReadOnly

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['departure_city', 'destination_city', 'departure_time', 'class']
    search_fields = ['airline', 'flight_number']
    ordering_fields = ['price', 'departure_time']
