"""This file sets up the urls for the wiki app."""
from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [

    path('wiki/articles', ArticleListView.as_view(), name='list'),
    path('wiki/article/<int:pk>', ArticleDetailView.as_view(), name='article_detail')
    
]

app_name = "wiki"
