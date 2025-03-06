"""Modules importing django views and Product from app models for url views."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductList(ListView):
    """Class viewing the list of products."""

    model = Product
    template_name = "items/items.html"

class ProductDetail(DetailView):
    """Class viewing a product in detail."""

    model = Product
    template_name = "item/item_detail.html"
