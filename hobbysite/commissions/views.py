"""This file sets up the views for the commissions app."""
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Commission


class CommissionListView(ListView):
    """Creates List View for the Commission model."""

    model = Commission
    template_name = 'commission_list.html'


class CommissionDetailView(DetailView):
    """Creates Detail View for the Commission model."""

    model = Commission
    template_name = 'commission_detail.html'
