"""Module importing the admin panels"""
from django.contrib import admin
from .models import Product, ProductType


class ProductTypeAdmin(admin.ModelAdmin):
    """Class for the Admin panel of ProductType model"""

    model = ProductType

class ProductAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Product model"""

    model = Product

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
