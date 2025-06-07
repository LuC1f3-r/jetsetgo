from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Booking(models.Model):
    BOOKING_TYPE = [
        ('flight', 'Flight'),
        ('hotel', 'Hotel'),
        ('car', 'Car'),
    ]
    STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    PAYMENT_STATUS = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=BOOKING_TYPE)
    reference_id = models.IntegerField()  # ID of hotel/flight/car
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='unpaid')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} Booking #{self.id}"
