"""This file sets up the urls for the wiki app."""
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [

    path('articles/', ArticleListView.as_view(), name='list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail')
    path('article/add', ArticleCreateView.as_view() , name='add'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view() , name='edit'),
    
]

app_name = "wiki"
