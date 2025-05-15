"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, PostListView, PostDetailView, PostCreateView, PostAddView

urlpatterns = [
    path('', index, name='index'),
    path('forum/threads', PostListView.as_view(), name='post-list'),
    path('forum/thread/<int:id>', PostDetailView.as_view(), name='post-detail'),
    path('forum/thread/add', PostCreateView.as_view(), name='post-create'),
    path('forum/thread/<int:pk>/edit', PostAddView.as_view(), name='post-add'),
]

app_name = "forum"