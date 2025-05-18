"""Module importing the admin panels"""
from django.contrib import admin
from .models import Product, ProductType, Transaction


class ProductTypeAdmin(admin.ModelAdmin):
    """Class for the Admin panel of ProductType model"""

    model = ProductType

class ProductAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Product model"""

    model = Product

class TransactionAdmin(admin.ModelAdmin):

    model = Transaction
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
