from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import BrandForm, CarForm

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

def cars_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = brand.cars.all()
    return render(request, 'cars/cars_list.html', {'brand': brand, 'cars': cars})

def new_car(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.brand = brand
            car.save()
        return redirect('cars_list', brand_id=brand_id)
    
    else:
        form = CarForm()
    
    return render(request, "cars/car_form.html", {'form': form, 'type_of_request': 'New'})

def edit_car(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('cars_list', brand_id=brand_id)
    else:
        form = CarForm(instance=car)
    
    return render(request, "cars/car_form.html", {'form': form, 'type_of_request': 'Edit'})