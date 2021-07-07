from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255)

    # Absolutely need __str__ b/c otherwise we won't know which brand a car belongs to, when creating a new car
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('Brand', on_delete=CASCADE, related_name='cars')
