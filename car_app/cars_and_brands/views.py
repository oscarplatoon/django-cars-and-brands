from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import BrandForm, CarForm

# display all brands
def brands(request):
    all_brands = Brand.objects.all()
    return render(request, 'brands.html', {'all_brands': all_brands})
    
def brand_detail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, 'brand_detail.html', {'brand': brand})

def new_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm()
    return render(request, 'brand_form.html', {'form': form, 'type': 'New'})

def brand_edit(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brand_form.html', {'form': form, 'type': 'Edit'})

def brand_delete(request, brand_id):
    if request.method == 'POST':
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    return redirect('brands')

def car_detail(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'brand': brand, 'car': car})

def new_car(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', brand_id=brand.id, car_id=car.id)
    else:
        form = CarForm(initial={'brand': brand})
    return render(request, 'car_form.html', {'form': form, 'type': 'New', 'brand': brand })
    
def car_edit(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', brand_id=brand.id, car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'car_form.html', {'form': form, 'type': 'Edit', 'brand': brand })

def car_delete(request, brand_id, car_id):
    if request.method == 'POST':
        car = Car.objects.get(id=car_id)
        car.delete()
    return redirect('brand_detail', brand_id=brand_id)

def cars(request):
    all_cars = Car.objects.all()
    return render(request, 'cars.html', {'all_cars': all_cars})