# The model is referring to multiple base model where the attributes of base class are shared among inherited class
# and object of base class along with the inherited class has its object created
from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'person'


class Employee(Person):
    eid = models.IntegerField(unique=True)
    salary = models.FloatField()
    role = models.CharField(max_length=10)

    class Meta:
        db_table = 'Employee'


class Address(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    empref = models.OneToOneField(Employee, on_delete=models.RESTRICT, unique=True)  # employee


def my_logic():
    all_emps = Employee.objects.all()
    if all_emps:
        return all_emps[0]  # last emp


class Roles(models.Model):
    role = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    empref = models.ForeignKey(Employee, on_delete=models.SET(my_logic), unique=False)  ##set of emps


class Skills(models.Model):  # id --> int
    skill = models.CharField(max_length=255)  # skill --->string
    code = models.CharField(max_length=255)  # code --> string
    empref = models.ManyToManyField(Employee)  # set of emps


class Student(Person):
    sid = models.IntegerField(default=1)
    sdept = models.CharField(max_length=20)
    scourse = models.CharField(max_length=20)

    class Meta:
        db_table = 'Student'
