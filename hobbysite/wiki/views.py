from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
