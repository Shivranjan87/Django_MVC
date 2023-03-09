from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    salary = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    role = models.CharField(max_length=255)

    class Meta:
        db_table = "EMPLOYEE_MVC_TABLE"


#e1 = Employee(id=0,name='',email='',salary=0,city='',state='',pincode='',role='')
