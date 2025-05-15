"""This file defines each view by referencing the models."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from .models import ThreadCategory, Thread, Comment, Profile
from .forms import Comment


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
            else:
                category_threads = {}
                
        ctx = {
            'user_threads': user_threads,
            'category_threads': category_threads,
        }

        return render(request, 'templates/thread_list.html', ctx)


class ThreadDetailView(LoginRequiredMixin, DetailView):
    """Views the details of the thread of posts."""

    model = Thread
    template_name = 'templates/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        thread = self.object
        category = thread.category
        other_threads = Thread.objects.filter(category=category).exclude(id=thread.id)
        comments = Comment.objects.filter(thread=thread).order_by('created_on')
        
        comment_form = CommentForm()

        ctx = {
            'other_threads': other_threads,
            'comments': comments,
            'comment_form': comment_form,
        }

        return render(request, 'templates/thread_detail.html', ctx)

    def post(self, request, *args, **kwargs):
        thread = self.get_object()

        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to comment.")
        
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.thread = thread
            c.author = Profile.objects.get(user=request.user)
            c.save()
            return redirect('thread_detail', pk=thread.id)
        else:
            ctx = self.get_context_data(**kwargs)
            ctx['comment_form'] = form
            return self.render_to_response(ctx)


class ThreadCreateView():
    """Views the 'create a thread' page."""

    model = Thread
    template_name = 'templates/thread_create.html'

    return render(request, 'templates/thread_detail.html', ctx)


class ThreadAddView():
    """Views the 'edit thread' page.""" 

    model = Thread
    template_name = 'templates/thread_add.html'

    return render(request, 'templates/thread_detail.html', ctx)
