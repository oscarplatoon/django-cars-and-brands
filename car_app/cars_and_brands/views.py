from django.shortcuts import render, redirect
from .forms import BrandForm, CarForm
from .models import Brand, Car

# Create your views here.
def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)

def brands_list(request):
    brands = Brand.objects.all()
    data = { 'all_brands': brands}
    return render(request, 'brand/brands_list.html', data)

def brand_detail(request, brand_id):
    brand = get_brand(brand_id)
    data = {'brand': brand}
    return render(request, 'brand/brand_detail.html', data)

def new_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm()
    return render(request, 'brand/brand_form.html', {'form': form, 'type_of_request': 'New'})

def edit_brand(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brand/brand_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_brand(request, brand_id):
    if request.method == "POST":
        brand = get_brand(brand_id)
        brand.delete()
    return redirect('brands_list')

# car controllers
def get_car(car_id):
    return Car.objects.get(id=car_id)

def cars_list(request, brand_id):
    brand = get_brand(brand_id)
    cars = brand.cars.all()
    return render(request, 'cars/cars_list.html', {'brand': brand, 'cars': cars})

def car_detail(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    return render(request, 'cars/car_detail.html', {'brand': brand, 'car': car})

def new_car(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.brand = brand
            car.save()
            return redirect('car_detail', brand_id=car.brand.id, car_id=car.id)
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form, 'type_of_request': 'New'})

def edit_car(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', car_id=car.id, brand_id=brand_id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_car(request, brand_id, car_id):
    if request.method == "POST":
        car = get_car(car_id)
        car.delete()
    return redirect('car_list', brand_id=brand_id)