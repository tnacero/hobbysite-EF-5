"""This file defines the url path for each view."""
from django.urls import path 
from .views import ThreadListView, ThreadDetailView

urlpatterns = [
    path('forum/threads', ThreadListView.as_view() , name='post-list'),
    path('forum/thread/<int:pk>', ThreadDetailView.as_view() , name='post-detail'),
]

app_name = "forum"
