from django.contrib import admin

# Register your models here.
from inventory.models import *

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Student)
