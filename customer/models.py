from django.db import models

# Create your models here.

class CustomerInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=45)
    gender = models.CharField(max_length=40,choices=[('M','Male'),('F','Female')])

    class Meta:
        db_table = "USER_CUSTOMER_MASTER"


class PersonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=45)
    gender = models.CharField(max_length=40,choices=[('M','Male'),('F','Female')])

    class Meta:
        db_table = "PERSON_MASTER"

class AuthorInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    numofbooks = models.IntegerField(default=0)
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=40,choices=[('M','Male'),('F','Female')])

    class Meta:
        db_table = "AUTHOR_MASTER"
       # ordering = [-'age']