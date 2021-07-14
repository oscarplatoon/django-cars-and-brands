from django.shortcuts import render, redirect, HttpResponse
from .forms import BrandForm
from .models import Brand

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