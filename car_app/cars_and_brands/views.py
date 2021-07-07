from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brand, Car
from .forms import BrandForm, CarForm

# helper methods


def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)


def get_car(car_id):
    return Car.objects.get(id=car_id)

# Routes for Brand


def show_brands(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'cars_and_brands/show_brands.html', context)


def new_brand(request):
    if request.method == 'POST':
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            new_brand = brand_form.save()
            return redirect('show_brand', brand_id=new_brand.id)
    else:
        brand_form = BrandForm()
        context = {'brand_form': brand_form, 'type_of_request': 'New'}

    return render(request, 'cars_and_brands/brand_form.html', context)


def show_brand(request, brand_id):
    brand = get_brand(brand_id)
    context = {'brand': brand}
    return render(request, 'cars_and_brands/show_brand.html', context)


def edit_brand(request, brand_id):
    brand = get_brand(brand_id)

    if request.method == 'POST':
        brand_form = BrandForm(request.POST, instance=brand)
        if brand_form.is_valid():
            updated_brand = brand_form.save()
            return redirect('show_brand', brand_id=updated_brand.id)
    else:
        brand_form = BrandForm(instance=brand)
        context = {'brand_form': brand_form, 'type_of_request': 'Edit'}

    return render(request, 'cars_and_brands/brand_form.html', context)

# Routes for Car


def list_cars(request, brand_id):
    brand = get_brand(brand_id)
    cars = brand.cars.all()
    context = {'brand': brand, 'cars': cars}

    return render(request, 'cars_and_brands/list_cars.html', context)


def show_car(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    context = {'brand': brand, 'car': car}

    return render(request, 'cars_and_brands/show_car.html', context)


def new_car(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == 'POST':
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            # commit=False b/c, before actually saving to the database, we wanna manually code in new_car's 'brand' property (rather than having it appear in the form)
            new_car = car_form.save(commit=False)
            new_car.brand = brand
            new_car.save()  # saves to db
            return redirect('show_car', brand_id=brand_id, car_id=new_car.id)
    else:
        car_form = CarForm()
        context = {'car_form': car_form,
                   'type_of_request': 'New', 'brand': brand}

    return render(request, 'cars_and_brands/car_form.html', context)


def edit_car(request, brand_id, car_id):
    car = get_car(car_id)
    brand = get_brand(brand_id)
    if request.method == 'POST':
        # CarForm(): 1st param getting the data the user entered in the CarForm; 2nd param is referring to which Car we'll be editing
        car_form = CarForm(request.POST, instance=car)
        if car_form.is_valid():
            new_car = car_form.save(commit=False)
            new_car.brand = brand
            new_car.save()
            return redirect('show_car', brand_id=brand_id, car_id=new_car.id)
    else:
        car_form = CarForm(instance=car)
        context = {'car_form': car_form,
                   'type_of_request': 'Edit', 'brand': brand}

    return render(request, 'cars_and_brands/car_form.html', context)


def delete_car(request, brand_id, car_id):
    car = get_car(car_id)
    car.delete()
    return redirect('list_cars', brand_id=brand_id)


def delete_brand(request, brand_id):
    brand = get_brand(brand_id)
    brand.delete()
    return redirect('show_brands')
