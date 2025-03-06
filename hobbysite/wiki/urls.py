from django.urls import path
from .views import WikiListView, WikiDetailView

urlpatterns = [

    path('/wiki/articles', WikiListView.as_view(), name='list'),
    path('/wiki/article/1', WikiDetailView.as_view(), name='wiki_detail')
    
]

app_name = "wiki"