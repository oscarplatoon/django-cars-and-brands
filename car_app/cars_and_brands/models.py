from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
class Car(models.Model):
    model = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
  
      
    def __str__(self):
        return f"{self.model}"
    
    # IF a car is made by 2 or more automakers
    # brand = models.ManyToManyField(Brand)
    # add --> if need thru-table (join table) --> , through="BrandCart")
    # then add:
    # class BrandCars(models.Model):
    #   car = models.ForeignKey()
    #   brand = models.ForeignKey()
    # unaware if need to add anything inside fk parentheses
    
    