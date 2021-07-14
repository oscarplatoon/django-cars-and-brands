from django.urls import path
from . import views

urlpatterns = [
    path('', views.brands_list, name='brands_list'),
    path('new', views.new_brand, name='new_brand'),
    path('<int:brands_id>', views.brands_detail, name='brands_detail'),
    path('<int:brands_id>/edit', views.edit_brand, name='edit_brand'),
    path('<int:brands_id>/delete', views.delete_brand, name='delete_brand'),
    # path('<int:cohort_id>/students', views.student_list, name='student_list'),
    # path('<int:cohort_id>/students/new', views.new_student, name='new_student'),
    # path('<int:cohort_id>/students/<int:student_id>', views.student_detail, name='student_detail'),
    # path('<int:cohort_id>/students/<int:student_id>/edit', views.edit_student, name='edit_student'),
    # path('<int:cohort_id>/students/<int:student_id>/delete', views.delete_student, name='delete_student'),
]