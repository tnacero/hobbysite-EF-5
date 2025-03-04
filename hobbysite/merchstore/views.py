"""Modules importing django views, HttpResponse and Product for url views."""
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

def index(request):
    """function printing homepage message."""
    return HttpResponse('Welcome to the merch store!')

class ProductList(ListView):
    """Class viewing the list of products."""

    model = Product
    template_name = "items/items.html"

class ProductDetail(DetailView):
    """Class viewing a product in detail."""

    model = Product
    template_name = "item/item_detail.html"
