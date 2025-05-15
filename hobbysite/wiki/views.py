"""This file sets up the views for the wiki app."""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .models import *
from .forms import *


class ArticleListView(ListView):
    """Creates List View for the ArticleCategory model."""
    
    model = ArticleCategory
    template_name = 'articles.html'


class ArticleDetailView(FormMixin, DetailView):
    """Creates Detail View for the Article model."""
    
    model = Article
    template_name = 'article_detail.html'
    form_class = WikiCommentForm
    
    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={'pk': self.get_object().pk})
    
    """For the Comment Form"""
    def get_context_data(self, **kwargs):
        ctx = super(ArticleDetailView, self).get_context_data(**kwargs)
        ctx['form'] = WikiCommentForm(initial={'post': self.object})
        return ctx
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView, self).form_valid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Creates Create View for the Article model"""
    
    model = Article 
    template_name = 'article_create.html' 
    form_class = WikiCreateForm
    success_url = '/wiki/articles/' 


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """Creates Update View for the Article model"""
    
    model = Article 
    template_name = 'article_update.html' 
    form_class = WikiUpdateForm
    
    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={'pk': self.get_object().pk})
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = WikiUpdateForm()
        return ctx