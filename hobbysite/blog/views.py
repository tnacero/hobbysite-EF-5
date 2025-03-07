from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory

class ArticleListView(ListView): 
    """Class for the list view of the articles"""
    model = ArticleCategory 
    template_name = 'articlelist.html' 

class ArticleDetailView(DetailView):
    """Class for the detail view of the articles"""
    model = Article 
    template_name = 'articles.html' 
