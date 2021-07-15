from django.urls import path
from  . import views

urlpatterns = [
    path('', views.brands, name='brands'),
    path('<int:brand_id>', views.brand_detail, name='brand_detail'),
    path('new', views.new_brand, name='new_brand')
]