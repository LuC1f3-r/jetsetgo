from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        booking_type = self.request.data.get('type')
        reference_id = self.request.data.get('reference_id')

        # Validate and check availability
        if booking_type == 'hotel':
            try:
                hotel = Hotel.objects.get(id=reference_id)
            except Hotel.DoesNotExist:
                raise ValidationError("Hotel not found.")
            if hotel.rooms_available < 1:
                raise ValidationError("No rooms available.")
            hotel.rooms_available -= 1
            hotel.save()

        elif booking_type == 'flight':
            try:
                flight = Flight.objects.get(id=reference_id)
            except Flight.DoesNotExist:
                raise ValidationError("Flight not found.")
            if flight.seats_available < 1:
                raise ValidationError("No seats available.")
            flight.seats_available -= 1
            flight.save()

        elif booking_type == 'car':
            try:
                car = Car.objects.get(id=reference_id)
            except Car.DoesNotExist:
                raise ValidationError("Car not found.")
            if not car.availability:
                raise ValidationError("Car is already booked.")
            car.availability = False
            car.save()

        else:
            raise ValidationError("Invalid booking type.")

        # Save booking with user info
        serializer.save(user=self.request.user)
