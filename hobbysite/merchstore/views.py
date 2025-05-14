"""Modules importing django views and Product from app models for url views."""
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from user_management.models import Profile
from .models import Product, ProductType ,Transaction
from .forms import ProductForm, TransactionForm


def product_list(request):
    """function viewing the list of products."""
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        user_products = Product.objects.filter(
            owner__user=request.user
        )
    else:
        user_products = None

    product_types =  ProductType.objects.all()

    ctx = {
        "user_products": user_products,
        "products": products,
        "product_types": product_types
    }   

    return render(request, "items/items.html", ctx)    

class ProductDetail(DetailView):
    """Class viewing a product in detail."""

    model = Product
    template_name = "item/item_detail.html"
    
    def post(self, request, *args, **kwargs):
        
        form = TransactionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                tr = Transaction()
                tr.buyer = request.user.profile
                tr.amount = form.cleaned_data.get('amount')
                tr.status = 'On Cart'
                product = self.get_object()
                product.stock -= tr.amount
                if product.stock < 1:
                    product.stock = 0
                    product.status = 'Out of Stock'
                tr.product = product
                tr.save()
                product.save()
                if product.stock < 0:
                    return self.get(request, *args, **kwargs)
                
                else: 
                    return redirect('merchstore:cart')
            else:
                return HttpResponseRedirect("/merchstore/{}".format(self.get_object().pk))

    def get_success_url(self):
         return reverse_lazy('merchstore:cart')

@login_required(redirect_field_name="registration/login.html")
def product_create(request):
    """Function used to create a product."""
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            i = Product()
            i.name = form.cleaned_data.get('name')
            i.product_type = form.cleaned_data.get('product_type')
            i.description = form.cleaned_data.get('description')
            i.price = form.cleaned_data.get('price')
            i.stock = form.cleaned_data.get('stock')
            i.status = form.cleaned_data.get('status')
            i.owner = Profile.objects.get(user=request.user)
            i.save()
            return redirect('merchstore:items')

    ctx = {"form": form}
    return render(request, 'item/add.html', ctx)

class ProductUpdate(LoginRequiredMixin, UpdateView):
    """
    Class to Update a product.
    """
    model = Product
    fields = [
        "name", "product_type", "description", "price", "stock", "status"
    ]
    template_name = "item/edit.html"

    def get_success_url(self):
        return reverse_lazy('merchstore:items')


    def form_valid(self, form):
        if form.instance.stock < 1:
            form.instance.status = "Out of Stock"
        return super().form_valid(form)
    redirect_field_name = "registration/login.html"    
    
@login_required(redirect_field_name="registration/login.html")
def cart(request):
    """function viewing the list of products."""
    transactions = Transaction.objects.all()
    
    
    if request.user.is_authenticated:
        user_cart = Transaction.objects.filter(
            buyer__user=request.user
        )
    else:
        user_cart = None

    owner_sort = defaultdict(list)

    for object in user_cart:
        owner_sort[object.product.owner].append(object)
    ctx = {
        "owner_sort": owner_sort.items(),
    }

    return render(request, "items/cart.html", ctx) 

@login_required(redirect_field_name="registration/login.html")
def transactions(request):
    """function viewing the list of products."""
    transaction_list = Transaction.objects.all()
    
    
    if request.user.is_authenticated:
        user_transac = Transaction.objects.filter(
            product__owner=request.user.profile
        )
    else:
        user_transac = None

    buyer_sort = defaultdict(list)

    for object in user_transac:
        buyer_sort[object.buyer].append(object)

    ctx = {
        "buyer_sort": buyer_sort.items(),
    }

    return render(request, "items/transactions.html", ctx) 