"""This file sets up the urls for the commissions app."""
from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list', CommissionListView.as_view(), name='commissions-list'),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name='commissions-detail'),
]

app_name = 'commissions'
