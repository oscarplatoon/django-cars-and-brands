from django.urls import path
from . import views

urlpatterns = [
    path('', views.brands_list, name='brands_list'),
    path('new', views.new_brand, name='new_brand'),
    path('<int:brands_id>', views.brands_detail, name='brands_detail'),
    path('<int:brands_id>/edit', views.edit_brand, name='edit_brand'),
    path('<int:brands_id>/delete', views.delete_brand, name='delete_brand'),
    path('<int:brands_id>/cars', views.cars_list, name='cars_list'),
    path('<int:brands_id>/cars/new', views.new_car, name='new_car'),
    path('<int:brands_id>/cars/<int:cars_id>', views.cars_detail, name='cars_detail'),
    path('<int:brands_id>/cars/<int:cars_id>/edit', views.edit_car, name='edit_car'),
    path('<int:brands_id>/cars/<int:cars_id>/delete', views.delete_car, name='delete_car'),
]