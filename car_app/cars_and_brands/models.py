from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Brand(models.Model):
    brand = models.CharField(max_length=200)

    def __str__(self):
        return f'Brand: {self.brand}'


class Car(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    color = models.CharField(max_length=200)

    def __str__(self):
        return (f"brand: {self.brand}, model: {self.model}, year: {self.year}, color: {self.color}")
