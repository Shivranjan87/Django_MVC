from django.contrib import admin

# Register your models here.
from customer.models import CustomerInfo, AuthorInfo

admin.site.register(CustomerInfo)
admin.site.register(AuthorInfo)