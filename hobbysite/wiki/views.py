"""This file sets up the views for the wiki app."""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, ArticleCategory, Comment
from .forms import WikiCreateForm, WikiUpdateForm, WikiCommentForm


class ArticleListView(ListView):
    """Creates List View for the ArticleCategory model."""
    
    model = ArticleCategory
    template_name = 'articles.html'


class ArticleDetailView(DetailView):
    """Creates Detail View for the Article model."""
    
    model = Article
    template_name = 'article_detail.html'
    form_class = WikiCommentForm
    
    def get_context_data(self, **kwargs): # Gets contexts for articles and comments
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated: # Compiles articles made by the current user
            ctx['common_articles'] = Article.objects.filter(author=self.request.user.profile)
        ctx['comments'] = Comment.objects.all()
        ctx['comment_form'] = self.form_class()
        ctx['articles'] = Article.objects.all()
        return ctx
    
    def form_valid(self, form): # Sets the author to the current user
        form.instance.article = self.get_object()
        form.instance.author = self.request.user.profile
        form.save()
        return redirect(self.request.path)

    def post(self, request, *args, **kwargs): # For the comment form
        form = WikiCommentForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Creates Create View for the Article model"""
    
    model = Article 
    template_name = 'article_create.html' 
    form_class = WikiCreateForm
    success_url = '/wiki/articles/' 
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile # Sets the author to the current user
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """Creates Update View for the Article model"""
    
    model = Article 
    template_name = 'article_update.html' 
    form_class = WikiUpdateForm
    
    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={'pk': self.get_object().pk})
    
    def get_context_data(self, **kwargs): # Gets context
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = WikiUpdateForm()
        return ctx
     
    def form_valid(self, form): # Sets the author to the current user
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)