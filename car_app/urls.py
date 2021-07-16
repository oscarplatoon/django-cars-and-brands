from django.contrib import admin
from django.urls import path, include
from cars_and_brands import views

urlpatterns = [
    path("", views.index, name="home"),
    path("/brands", views.brands, name="brand_list")# a list of all the car brands
    path/("brands/new", views.brand_new, name="brand_new")# form for a new car brand
    path("/brands/<:id>", views.brand_detail, name="brand_detail") # see a specific car brand
    path("/brands/<:id>/edit", views.brand_edit, name ="brand_edit") # edit page for a specific car brand
    path("/brands/<:brand_id>/cars", views.models, name="model_list") # a list of cars for a specific car brand
    path("/brands/<:brand_id>/cars/new", views.model_new, name="model_new") # form for a new car under a specific car brand
    path("/pathbrands/<:brand_id>/cars/<:car_id>", views.model_detail, name="model_detail") # see a specific car for a specific car brand
    path("/brands/<:brand_id>/cars/<:car_id>/edit", views.model_edit, name="model_edit")# edit page for a specific car under a specific car brand
]


