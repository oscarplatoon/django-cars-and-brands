from django.db import models

class Brands(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, Title: {self.title}"

class Cars(models.Model):
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=200)
    type_model = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id} Make: {self.make}"