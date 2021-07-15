from django import forms
from .models import Brands, Cars

class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ('title', 'description')

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ('brand_name', 'make', 'type_model')