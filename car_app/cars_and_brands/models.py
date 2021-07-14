from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text

# Create your models here.
def validate_brand_name_presence(name):
    if len(name) == 0:
        raise ValidationError(text(
            'This field cannot be blank.'
        ))

def validate_car_name_presence(name):
    if len(name) == 0:
        raise ValidationError(text(
            'This field cannot be blank.'
        ))

def validate_car_year_presence(year):
    if len(year) == 0:
        raise ValidationError(text(
            'This field cannot be blank.'
        ))


class Brand(models.Model):
    name = models.CharField(max_length=200, validators=[validate_brand_name_presence])

    def __str__(self) -> str:
        return f"ID: {self.id} Name: {self.name}"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')

    name = models.CharField(max_length=200, validators=[validate_car_name_presence])
    year = models.CharField(max_length=200, validators=[validate_car_year_presence])

    def __str__(self) -> str:
        return f"ID: {self.id} Name: {self.name} Year: {self.year}"
