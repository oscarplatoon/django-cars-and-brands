from django.forms import ModelForm
from .models import Brand, Car


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name']
        # 'brand' is excluded b/c the form is for a new car under a specific brand, so no need for user to specify 'brand'
        exclude = ['brand']
