"""This file defines each view by referencing the models."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import ThreadCategory, Thread


class ThreadListView(TemplateView):
    """Views the posts' category."""

    model = ThreadCategory
    template_name = 'templates/thread_list.html'

    def thread_list(request):
        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
            user_threads = Thread.objects.filter(author=profile)
            all_threads = Thread.objects.exclude(author=profile)

        else:
            user_threads = Thread.objects.none()
            all_threads = Thread.objects.all()

        category_threads = {}
        for category in ThreadCategory.objects.all():
            threads_in_category = all_threads.filter(category=category)
            if threads_in_category.exists():
                category_threads[category] = threads_in_category

        ctx = {
            'user_threads': user_threads,
            'category_threads': category_threads,
        }

        return ctx


class ThreadDetailView(DetailView):
    """Views the details of the thread of posts."""

    model = Thread
    template_name = 'templates/thread_detail.html'


class ThreadCreateView():
    """Views the 'create a thread' page."""

    model = Thread
    template_name = 'templates/thread_create.html'


class ThreadAddView():
    """Views the 'edit thread' page.""" 

    model = Thread
    template_name = 'templates/thread_add.html'
