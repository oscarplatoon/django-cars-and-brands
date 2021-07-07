from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_brands, name='show_brands'),
    path('new/', views.new_brand, name='new_brand'),
    path('<int:brand_id>/', views.show_brand, name='show_brand'),
    path('<int:brand_id>/edit/', views.edit_brand, name='edit_brand'),
    path('<int:brand_id>/cars/', views.list_cars, name='list_cars'),
    path('<int:brand_id>/cars/<int:car_id>/', views.show_car, name='show_car'),
    path('<int:brand_id>/cars/new/', views.new_car, name='new_car'),
    path('<int:brand_id>/cars/<int:car_id>/edit/',
         views.edit_car, name='edit_car'),
    path('<int:brand_id>/cars/<int:car_id>/delete/',
         views.delete_car, name='delete_car'),
    path('<int:brand_id>/delete/', views.delete_brand, name='delete_brand'),
]
