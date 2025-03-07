"""This file defines the url path for each view."""
from django.urls import path 
from .views import PostListView, PostDetailView

urlpatterns = [
    path('threads', PostListView.as_view() , name='post-list'),
    path('thread/<int:pk>', PostDetailView.as_view() , name='post-detail'),
]

app_name = "forum"
