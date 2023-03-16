from django.contrib import admin

# Register your models here.
from app1.models import Person, Person_Proxy

admin.site.register(Person)
admin.site.register(Person_Proxy)