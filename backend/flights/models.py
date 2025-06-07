from django.db import models

# Create your models here.
class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=50, unique=True)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    CLASS_CHOICES = [('economy', 'Economy'), ('business', 'Business'), ('first', 'First')]
    flight_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    seats_available = models.IntegerField()

    def __str__(self):
        return f"{self.airline} {self.flight_number}"