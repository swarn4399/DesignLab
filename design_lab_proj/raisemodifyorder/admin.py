from django.contrib import admin
from .models import FoodSeeker,Addresses,Order

# Register your models here.
admin.site.register(FoodSeeker)
admin.site.register(Addresses)
admin.site.register(Order)

