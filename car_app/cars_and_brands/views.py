from django.shortcuts import render, redirect, HttpResponse
from .models import Brands, Cars
from .forms import BrandsForm, CarsForm


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

# Cars

def get_car(cars_id):
    return Cars.objects.get(id=cars_id)

def cars_list(request, brands_id):
    car = Cars.objects.all()
    return render(request, 'brands/cars_list.html', {'car': car})

def cars_detail(request, brands_id, cars_id):
    brand = get_brand(brands_id)
    car = get_car(cars_id)
    return render(request, 'brands/car_detail.html', {'brand': brand, 'car': car})

def new_car(request, brands_id):
    brand = get_brand(brands_id)
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.brand = brand
            car.save()
            return redirect('cars_detail', brands_id=car.brands.id, cars_id=car.id)
    else:
        form = CarsForm()
    return render(request, 'brands/cars_form.html', {'form': form, 'type_of_request': 'New'})

def edit_car(request, brands_id, cars_id):
    brand = get_brand(brands_id)
    car = get_car(cars_id)
    if request.method == "POST":
        form = CarsForm(request.POST, instance=car)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('car_detail', cars_id=car.id, brands_id=brands_id)
    else:
        form = CarsForm(instance=car)
    return render(request, 'brands/cars_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_car(request, brands_id, cars_id):
    if request.method == "POST":
        car = get_car(cars_id)
        car.delete()
    return redirect('cars_list', brands_id=brands_id)