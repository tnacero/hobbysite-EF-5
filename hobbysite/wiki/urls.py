from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [

    path('/wiki/articles', ArticleListView.as_view(), name='list'),
    path('/wiki/article/1', ArticleDetailView.as_view(), name='article_detail')
    
]

app_name = "wiki"
