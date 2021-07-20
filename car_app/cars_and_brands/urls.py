from django.urls import path
from  . import views

urlpatterns = [
    
    # Brands URL
    path('', views.brands, name='brands'),
    path('<int:brand_id>', views.brand_detail, name='brand_detail'),
    path('new', views.new_brand, name='new_brand'),
    path('<int:brand_id>/edit', views.brand_edit, name='brand_edit'),
    path('<int:brand_id>/delete', views.brand_delete, name='brand_delete'),
    
    # Cars URL
    path('<int:brand_id>/cars/<int:car_id>', views.car_detail, name='car_detail'),
    path('<int:brand_id>/cars/new', views.new_car, name='new_car'),
    path('<int:brand_id>/cars/<int:car_id>/edit', views.car_edit, name='car_edit'),
    path('<int:brand_id>/cars/<int:car_id>/delete', views.car_delete, name='car_delete'),
    path('cars', views.cars, name='cars')
]