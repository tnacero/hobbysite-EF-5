"""Module providing a function redirecting urls to merch store."""

from django.urls import path
from .views import product_list, ProductDetail, product_create, ProductUpdate, cart, transactions
urlpatterns = [
    path('', product_list, name= 'items'),
    path('add', product_create, name= 'add'),
    path('<int:pk>/edit', ProductUpdate.as_view(), name= 'edit'),
    path('cart', cart, name= 'cart'),
    path('transactions', transactions, name= 'transactions'),
    path('<int:pk>', ProductDetail.as_view(), name = "item-detail"),
]
app_name = 'merchstore'
