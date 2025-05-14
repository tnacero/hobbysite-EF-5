from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class ArticleListView(ListView): 
    """Class for the list view of the articles"""
    model = ArticleCategory 
    template_name = 'blog_list.html' 

class ArticleDetailView(DetailView):
    """Class for the detail view of the articles"""
    model = Article 
    template_name = 'blog_detail.html' 
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Class for the creation of the articles"""
    model = Article 
    template_name = 'blog_create.html' 
    fields = ['title', 'category', 'entry'] 
    success_url = '/blog/articlelist/' 

