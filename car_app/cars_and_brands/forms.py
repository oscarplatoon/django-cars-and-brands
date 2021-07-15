from django import forms
from django.db import models
from django.forms import fields
from .models import Brand, Car


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand']