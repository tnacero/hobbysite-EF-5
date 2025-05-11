"""Modules importing django views and Product from app models for url views."""
from django.urls import reverse_lazy
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Transaction
from .forms import ProductForm, TransactionForm

class ProductList(ListView):
    """Class viewing the list of products."""

    model = Product
    template_name = "items/items.html"

class ProductDetail(UpdateView):
    """Class viewing a product in detail."""

    model = Product
    template_name = "item/item_detail.html"
    form_class = TransactionForm
    def get_success_url(self):
        return reverse_lazy('merchstore:cart')

class ProductCreate(LoginRequiredMixin, CreateView):
    """
    Class to create a new product.
    """
    model = Product
    template_name = "item/add.html"
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse_lazy('merchstore:items')
    redirect_field_name = "registration/login.html"

class ProductUpdate(LoginRequiredMixin, UpdateView):
    """
    Class to Update a product.
    """
    model = Product
    template_name = "item/edit.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('merchstore:items')
    redirect_field_name = "registration/login.html"

class Cart(ListView):
    """
    This class is to view the current products available in the cart.
    """
    model = Transaction
    template_name = "items/cart.html"

class Transactions(ListView):
    """
    This class is to show the list of transactions currently available.
    """
    model = Transaction
    template_name = "items/transactions.html"
