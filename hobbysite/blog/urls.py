from django.urls import path 
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles', ArticleListView.as_view() , name='article-list'), # URL for article list
    path('article/<int:pk>', ArticleDetailView.as_view() , name='article-detail'), # URL for article detail
    path('article/add', ArticleCreateView.as_view() , name='article-add'), # URL for adding new blogs
    path('article/<int:pk>/edit', ArticleUpdateView.as_view() , name='article-edit'), # URL for editings existing blogs
]

app_name = "blog"