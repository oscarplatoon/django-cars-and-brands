from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars_and_brands.models import CarBrand, CarModel
from cars_and_brands.forms import CarBrandForm, CarModelForm

def index(request):
    return render(request, "pages/home.html")

#brand
def brands(request):
    data = {
        "brands": CarBrand.objects.all()
    }
    return render(request, "pages/brands/brand_list.html", data)

def brand_new(request):
    form = CarBrandForm(request.POST or None)

    if request.method == "POST":
        try:
            form.save()
            return redirect("cars:brand_list")
        except:
            return HttpResponse("Error creating new brand!")

    data = {
        "create_or_update": True,
        "form": form
    }
    return render(request, "pages/brands/brand_form.html", data)

def brand_detail(request, brand_id):
    try:
        brand = CarBrand.objects.get(pk=brand_id)
    except:
        print("error")
        return HttpResponse("That car brand doesn't exist!")
    
    data = {
        "brand": brand
    }
    return render(request, "pages/brands/brand_detail.html", data)

def brand_edit(request, brand_id):
    try:
        brand = CarBrand.objects.get(pk=brand_id)
    except:
        print("error")
        return HttpResponse("That car brand doesn't exist!")
    
    form = CarBrandForm(request.POST or None, instance=brand)

    if request.method == "POST":
        try:
            form.save()
            return redirect("cars:brand_detail", brand_id=brand_id)
        except Exception as e:
            print(e)
            return HttpResponse("Error updating new brand!")

    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "pages/brands/brand_form.html", data)

# models
def models(request, brand_id):
    try:
        brand = CarBrand.objects.get(pk=brand_id)
    except:
        print("error")
        return HttpResponse("That car brand doesn't exist!")
    
    data = {
        "brand": brand
    }
    return render(request, "pages/models/model_list.html", data)

def model_new(request, brand_id):
    try:
        brand = CarBrand.objects.get(pk=brand_id)
    except:
        print("error")
        return HttpResponse("That car brand doesn't exist!")

    form = CarModelForm(request.POST or None, initial={"brand": brand})

    if request.method == "POST":
        try:
            form.save()
            return redirect("cars:model_list", brand_id=form.instance.brand.id)
        except Exception as e:
            print(e)
            return HttpResponse("Error adding new model") 

    data = {
        "create_or_update": True,
        "form": form
    }
    return render(request, "pages/models/model_form.html", data)

def model_detail(request, brand_id, model_id):
    try:
        model = CarModel.objects.get(pk=model_id)
    except:
        print("error")
        return HttpResponse("That car model doesn't exist!")
    
    data = {
        "model": model
    }
    return render(request, "pages/models/model_detail.html", data)

def model_edit(request, brand_id, model_id):
    try:
        model = CarModel.objects.get(pk=model_id)
    except:
        print("error")
        return HttpResponse("That car model doesn't exist!")

    form = CarModelForm(request.POST or None, instance=model)

    if request.method == "POST":
        try:
            form.save()
            return redirect("cars:model_detail", brand_id=brand_id, model_id=model_id)
        except Exception as e:
            print(e)
            return HttpResponse("Error adding new model") 

    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "pages/models/model_form.html", data)


