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