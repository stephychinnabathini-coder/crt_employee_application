from django.urls import path
from .views import add_employee,get_employee_details

urlpatterns = [
    path('add_emp',add_employee),
    path('get_data',get_employee_details)
]