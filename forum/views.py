"""This file defines each view by referencing the models."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import ThreadCategory, Thread


class ThreadListView(ListView):
    """Views the thread's category."""

    model = ThreadCategory
    template_name = 'templates/thread_list.html'


class ThreadDetailView(DetailView):
    """Views the details of the thread of threads."""

    model = Thread
    template_name = 'templates/thread_detail.html'

class ThreadCreateView():
    

class ThreadAddView():

