"""This file defines the url path for each view."""
from django.urls import path 
from .views import ThreadListView, ThreadDetailView

urlpatterns = [
    path('forum/threads', ThreadListView.as_view() , name='post-list'),
    path('forum/thread/<int:pk>', ThreadDetailView.as_view() , name='post-detail'),
    path('forum/thread/add', ThreadCreateView.as_view(), name='thread-create'),
    path('forum/thread/<int:pk>/edit', ThreadAddView.as_view(), name='thread-add'),
]

app_name = "forum"
