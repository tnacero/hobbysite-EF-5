"""Module providing a function redirecting urls to merch store."""

from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, Cart, Transactions
urlpatterns = [
    path('', ProductList.as_view(), name= 'items'),
    path('add', ProductCreate.as_view(), name= 'add'),
    path('edit', ProductUpdate.as_view(), name= 'edit'),
    path('cart', Cart.as_view(), name= 'cart'),
    path('transactions', Transactions.as_view(), name= 'transactions'),
    path('<int:pk>', ProductDetail.as_view(), name = "item-detail"),
]
app_name = 'merchstore'
