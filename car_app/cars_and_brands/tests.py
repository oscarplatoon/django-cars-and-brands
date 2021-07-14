from django.core import exceptions
from django.test import TestCase
from .models import *


# Create your tests here.
class AssociationTestCase(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create()
        self.car = Car.objects.create(brand=self.brand)

    def test01_brand_of_car(self):
        "returns the brand of the car"
        self.assertEqual(self.car.brand, self.brand)
    
    def test02_brand_cars(self):
        self.assertEqual(list(self.brand.cars.all()), [self.car])

class ValidationsTestCase(TestCase):

    brand = Brand()
    car = Car()

    def test01_validate_brand_name(self):
        try:
            self.brand.full_clean()
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['name'])

    def test02_validate_car_name(self):
        try:
            self.car.full_clean()
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['name'])

    def test03_validate_car_year(self):
        try:
            self.car.full_clean()
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['year'])