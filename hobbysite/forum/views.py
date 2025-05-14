"""This file defines each view by referencing the models."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import ThreadCategory, Thread


class ThreadListView(ListView):
    """Views the posts' category."""

    model = ThreadCategory
    template_name = 'thread_list.html'


class ThreadDetailView(DetailView):
    """Views the details of the thread of posts."""

    model = Thread
    template_name = 'thread_detail.html'

class ThreadCreateView():
    """ """

class ThreadAddView():
    """ """