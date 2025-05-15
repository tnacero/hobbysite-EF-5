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
from django.contrib import admin
from django.urls import include, path
from .views import ThreadListView, ThreadDetailView, ThreadCreateView, ThreadAddView

urlpatterns = [
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
    path('commissions/', include('commissions.urls', namespace = 'commissions')),
    path('blog/', include('blog.urls', namespace="blog")),
    path('wiki/', include('wiki.urls', namespace = 'wiki')),
    path('forum/', include('forum.urls', namespace="forum")),
    path('forum/threads', ThreadListView.as_view(), name='thread-list'),
    path('forum/thread/<int:id>', ThreadDetailView.as_view(), name='thread-detail'),
    path('forum/thread/add', ThreadCreateView.as_view(), name='thread-create'),
    path('forum/thread/<int:pk>/edit', ThreadAddView.as_view(), name='thread-add'),
    path('profile/', include('user_management.urls', namespace='profile')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls', namespace='home')),
]
