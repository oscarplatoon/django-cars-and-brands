from django.urls import path
from . import views

urlpatterns = [
    path('', views.brand_list, name='brand_list'),
    path('<int:brand_id>', views.model_list, name='model_list'),
    path('<int:brand_id>/add_brand', views.add_brand, name='add_brand'),
    path('<int:brand_id>/delete_brand', views.delete_brand, name='delete_brand'),
    path('<int:brand_id>/edit_car', views.edit_car, name='edit_car'),
]
