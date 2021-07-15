from django.shortcuts import render, redirect, HttpResponse
from .models import Brands, Cars
from .forms import BrandsForm, CarsForm


def get_brand(brand_id):
    return Brands.objects.get(id=brand_id)

def brands_list(request):
    brands = Brands.objects.all()
    return render(request, 'brands/brands_list.html', {'brands': brands})

def brands_detail(request, brand_id):
    brands = get_brand(brand_id)
    return render(request, 'brands/brands_detail.html', {'brands': brands})

def new_brand(request):
    if request.method == "POST":
        form = BrandsForm(request.POST)
        if form.is_valid():
            brands = form.save(commit=False)
            brands.save()
            return redirect('brands_detail', brand_id=brands.id)
    else:
        form = BrandsForm()
    return render(request, 'brands/brands_form.html', {'form': form, 'type_of_request': 'New'})

def delete_brand(request, brand_id):
    if request.method == "POST":
        brands = get_brand(brand_id)
        brands.delete()
    return redirect('brands_list')

def edit_brand(request, brand_id):
    brands = get_brand(brand_id)
    if request.method == "POST":
        form = BrandsForm(request.POST, instance=brands)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('brands_detail', brand_id=brands.id)
    else:
        form = BrandsForm(instance=brands)
    return render(request, 'brands/brands_form.html', {'form': form, 'type_of_request': 'Edit'})

# Cars

def get_car(car_id):
    return Cars.objects.get(id=car_id)

def cars_list(request, brand_id):
    brand = get_brand(brand_id)
    cars = brand.cars.all()
    context = {'brand': brand, 'cars': cars}
    return render(request, 'brands/cars_list.html', context)

def cars_detail(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    return render(request, 'brands/cars_detail.html', {'brand': brand, 'car': car})

def new_car(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.brand = brand
            car.save()
            return redirect('cars_detail', brand_id=car.brand.id, car_id=car.id)
    else:
        form = CarsForm()
    return render(request, 'brands/cars_form.html', {'form': form, 'type_of_request': 'New'})

def edit_car(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    if request.method == "POST":
        form = CarsForm(request.POST, instance=car)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('car_detail', car_id=car.id, brand_id=brand_id)
    else:
        form = CarsForm(instance=car)
    return render(request, 'brands/cars_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_car(request, brand_id, car_id):
    if request.method == "POST":
        car = get_car(car_id)
        car.delete()
    return redirect('cars_list', brand_id=brand_id)