from django.views.generic.list import ListView
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
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "blog_update.html"
    form_class = ArticleUpdateForm

    def form_valid(self, form):
        article = self.get_object() # Gets the article then passes it to the instance 
        form.instance.article = article
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

