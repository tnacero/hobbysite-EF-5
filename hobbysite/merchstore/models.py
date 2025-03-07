"""Module providing a base of models for python."""

from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    """Class representing a product type."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Function returning product type name."""
        return self.name
    
    def __str__(self):
        """returning description text field."""
        return self.description

    def get_absolute_url(self):
        """Function returning url of product type details."""
        return reverse('product_type_detail', args=[str(self.pk)])

class Product(models.Model):
    """Class representing a product from a product type."""

    
    name = models.CharField(max_length=255)
    ProductType = models.ForeignKey( 
        ProductType, on_delete=models.SET_NULL, null=True,
        related_name='product',)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        """Function returning product name."""
        return self.name
    
    def __str__(self):
        """returning description text field."""
        return self.description
    
    def __float__(self):
        return self.price

    def get_absolute_url(self):
        """Function returning url of product details."""
        return reverse('merchstore:item-detail', args=[str(self.pk)])
