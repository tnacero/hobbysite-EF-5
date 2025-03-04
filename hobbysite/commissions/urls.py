from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('/list', CommissionListView.as_view(), name='commission-list'),
    path('/detail/<int:pk>', CommissionDetailView.as_view(), name='commissions-detail'),
]

app_name = 'commissions'