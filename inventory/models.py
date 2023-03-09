from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    salary = models.FloatField()


class Address(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    empref = models.OneToOneField(Employee,on_delete=models.RESTRICT,unique=True)   #employee

def my_logic():
    all_emps = Employee.objects.all()
    if all_emps:
        return all_emps[0]     # last emp

class Roles(models.Model):
    role = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    empref = models.ForeignKey(Employee,on_delete=models.SET(my_logic),unique=False) ##set of emps


class Skills(models.Model):                   #id --> int
    skill = models.CharField(max_length=255)  #skill --->string
    code = models.CharField(max_length=255)   #code --> string
    empref = models.ManyToManyField(Employee)   #set of emps
