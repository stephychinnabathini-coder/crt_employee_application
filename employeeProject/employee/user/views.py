import json
from http import HTTPStatus
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeeModel


@csrf_exempt
def add_employee(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        emp_data = EmployeeModel.objects.create(
            id=data.get("id"),
            name=data.get("name"),
            email=data.get("email"),
            phone_no=data.get("phone_no"),
            address=data.get("address"),
            designation=data.get("designation"),
            emp_type=data.get("emp_type"),
        )

        return JsonResponse({
            "message": "Employee Added Successfully",
            "employee_id": emp_data.id,
            "status": HTTPStatus.OK,
        })


def get_employee_details(request):

    emp_data = EmployeeModel.objects.all().values()

    return JsonResponse({
        "data": list(emp_data),
        "status": HTTPStatus.OK,
    })