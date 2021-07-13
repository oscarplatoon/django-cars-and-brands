from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import BrandForm

def brands_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brands_list.html', {'brands': brands})

def new_brand(request):
    if request.method =="POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('/brands')
    else:
        form = BrandForm()
    
    return render(request, 'brands/brand_form.html', {'form': form, 'type_of_request': 'New'})


def edit_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method =="POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('/brands')
    else:
        form = BrandForm(instance=brand)
    
    return render(request, 'brands/brand_form.html', {'form': form, 'type_of_request': 'Edit'})