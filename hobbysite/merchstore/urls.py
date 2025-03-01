"""Module providing a function redirecting urls to recipe book."""

from django.urls import path
from .views import index, ProductList, ProductDetail
urlpatterns = [
    path('', index, name='index'),
    path('items', ProductList.as_view(), name= 'recipe-list'),
    path('items/<int:pk>', ProductDetail.as_view(), name = "recipe-detail"),
]
# This might be needed, depending on your Django version
app_name = 'merchstore'