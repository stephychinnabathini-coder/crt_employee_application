from django.db import models

class EmployeeModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=55)
    phone_no = models.BigIntegerField()
    address = models.CharField(max_length=100,default="unknown")
    designation = models.CharField(max_length=100)
    emp_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name