from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name', 'year')