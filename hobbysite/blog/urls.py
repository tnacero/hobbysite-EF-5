from django.urls import path 
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles', ArticleListView.as_view() , name='article-list'), # URL for article list
    path('article/<int:pk>', ArticleDetailView.as_view() , name='article-detail'), # URL for article detail
]

app_name = "blog"