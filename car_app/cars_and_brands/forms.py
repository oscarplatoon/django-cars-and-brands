from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('brand_name',)
