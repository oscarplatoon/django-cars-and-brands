from django.db import models
from django.db.models.deletion import CASCADE

class Brand(models.Model):
    brand_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.brand_name}"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=CASCADE, related_name="cars")
    model_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.model_name}"
