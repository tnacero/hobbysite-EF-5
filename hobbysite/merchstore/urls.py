"""Module providing a function redirecting urls to recipe book."""

from django.urls import path
from .views import ProductList, ProductDetail
urlpatterns = [
    path('merchstore/', ProductList.as_view(), name= 'items'),
    path('merchstore/<int:pk>', ProductDetail.as_view(), name = "item-detail"),
]
# This might be needed, depending on your Django version
app_name = 'merchstore'