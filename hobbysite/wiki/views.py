"""This file sets up the views for the wiki app."""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    """Creates List View for the Article model."""
    
    model = Article
    template_name = 'articles/articles.html'


class ArticleDetailView(DetailView):
    """Creates Detail View for the ArticleCategory model."""
    
    model = ArticleCategory
    template_name = 'article/article_detail.html'

