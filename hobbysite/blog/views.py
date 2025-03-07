from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory

class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'articlelist.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles.html'
