"""Module providing a base of models for python."""

from django.db import models
from django.urls import reverse
from user_management.models import Profile

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

    available = 'Available'
    on_sale = 'On sale'
    out_of_stock = 'Out of Stock'

    statuses = (
        (available, 'Available'),
        (on_sale, 'On sale'),
        (out_of_stock, 'Out of stock')
    )

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey( 
        ProductType, on_delete=models.SET_NULL, null=True,
        related_name='product',)
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True
        )
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField(default=1)
    status = models.CharField(max_length=255, choices=statuses ,default=available)

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

class Transaction(models.Model):
    """Class representing a transaction for each transaction made."""
    on_cart = 'On Cart'
    to_pay = 'To Pay'
    to_ship = 'To Ship'
    to_recieve = 'To Recieve'
    delivered = 'Delivered'

    statuses = (
        (on_cart, 'On Cart'),
        (to_pay, 'To Pay'),
        (to_ship, 'To Ship'),
        (to_recieve, 'To Recieve'),
        (delivered, 'Delivered')
    )
    buyer = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True
    )
    amount = models.IntegerField()
    status = models.CharField(max_length=255, choices=statuses ,default=None)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    