from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    rooms_available = models.IntegerField()
    amenities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
