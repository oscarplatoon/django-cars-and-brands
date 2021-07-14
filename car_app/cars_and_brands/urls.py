# /brands # a list of all the car brands
# /brands/new # form for a new car brand
# /brands/<:id> # see a specific car brand
# /brands/<:id>/edit # edit page for a specific car brand

# /brands/<:brand_id>/cars # a list of cars for a specific car brand
# /brands/<:brand_id>/cars/new # form for a new car under a specific car brand
# /brands/<:brand_id>/cars/<:car_id> # see a specific car for a specific car brand
# /brands/<:brand_id>/cars/<:car_id>/edit # edit page for a specific car under a specific car brand

from django.urls import path
from . import views

urlpatterns = [
    path('', views.brands_list, name='brands_list'),
    path('new', views.new_brand, name='new_brand'),
   # path('<int:brand_id>', views.brand_details, name='brand_details'),
    path('<int:brand_id>/edit', views.edit_brand, name='edit_brand'),
    path('<int:brand_id>/cars', views.cars_list, name='cars_list'),
    path('<int:brand_id>/cars/new', views.new_car, name='new_car'),
    path('<int:brand_id>/cars/<int:car_id>/edit', views.edit_car, name='edit_car'),  

]
