from django.shortcuts import render, redirect, HttpResponse
from .models import Brands
from .forms import BrandsForm


def get_brand(brands_id):
    return Brands.objects.get(id=brands_id)

def brands_list(request):
    brands = Brands.objects.all()
    return render(request, 'brands/brands_list.html', {'brands': brands})

def brands_detail(request, brands_id):
    brands = get_brand(brands_id)
    return render(request, 'brands/brands_detail.html', {'brands': brands})

def new_brand(request):
    if request.method == "POST":
        form = BrandsForm(request.POST)
        if form.is_valid():
            brands = form.save(commit=False)
            brands.save()
            return redirect('brands_detail', brands_id=brands.id)
    else:
        form = BrandsForm()
    return render(request, 'brands/brands_form.html', {'form': form, 'type_of_request': 'New'})

def delete_brand(request, brands_id):
    if request.method == "POST":
        brands = get_brand(brands_id)
        brands.delete()
    return redirect('brands_list')

def edit_brand(request, brands_id):
    brands = get_brand(brands_id)
    if request.method == "POST":
        form = BrandsForm(request.POST, instance=brands)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('brands_detail', brands_id=brands.id)
    else:
        form = BrandsForm(instance=brands)
    return render(request, 'brands/brands_form.html', {'form': form, 'type_of_request': 'Edit'})