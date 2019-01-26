from django.contrib import admin

# Register your models here.
from .models import Product, Choice, ShoppingCart

admin.site.register(Product)
admin.site.register(Choice)
admin.site.register(ShoppingCart)
