# The model is referring to abstract base model where the attributes of abstract class are shared among inherited class
# and object of base class is not created instead the class which is inherited has its object created
from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'persons'
        abstract = True
        ordering = ['age']


class Teacher(Person):
    tid = models.IntegerField()
    tqual = models.CharField(max_length=40,
                             choices=[('BE', 'Bachelor of Engineering'), ('ME', 'Masters of Engineering'),
                                      ('MCA', 'Masters of Computer Applications'), ('M.Pharm', 'Masters of Pharmacy')])
    tsal = models.FloatField()

    class Meta:
        db_table = 'Teacher_Abstract'
