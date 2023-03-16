# The model is referring to proxy base model where the attributes of proxy class and inherited class will not have any object created in database and base class object is created
from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'persons'


class Person_Proxy(Person):
    class Meta:
        db_table = 'persons_proxy'
        proxy = True
        ordering = ['age']
