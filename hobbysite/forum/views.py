"""This file defines each view by referencing the models."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import PostCategory, Post


class PostListView(ListView):
    """Views the posts' category."""

    model = PostCategory
    template_name = 'thread_list.html'


class PostDetailView(DetailView):
    """Views the details of the thread of posts."""

    model = Post
    template_name = 'thread_detail.html'
