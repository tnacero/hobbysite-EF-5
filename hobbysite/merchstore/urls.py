"""Module providing a function redirecting urls to merch store."""

from django.urls import path
from .views import ProductList, ProductDetail
urlpatterns = [
    path('merchstore/', ProductList.as_view(), name= 'items'),
    path('merchstore/<int:pk>', ProductDetail.as_view(), name = "item-detail"),
]
app_name = 'merchstore'
