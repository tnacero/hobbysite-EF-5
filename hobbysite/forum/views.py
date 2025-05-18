"""This file defines each view by referencing the models."""
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ThreadCategory, Thread, Comment, Profile


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
        other_threads = Thread.objects.filter(category=category).exclude(id=thread.id)[:2]
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
            return redirect('thread-detail', pk=thread.id)
        else:
            ctx = self.get_context_data(**kwargs)
            ctx['comment_form'] = form
            return self.render_to_response(ctx)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    """Views the 'create a thread' page."""

    model = Thread
    template_name = 'templates/thread_create.html'
    fields = ['title', 'category', 'entry', 'image']

    def get_queryset(self):
        return Thread.objects.filter(author__user=self.request.user)
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse_lazy('thread-detail', kwargs={'pk': self.object.pk})


class ThreadEditView(LoginRequiredMixin, UpdateView):
    """Views the 'edit thread' page.""" 

    model = Thread
    template_name = 'templates/thread_edit.html'
    fields = ['title', 'category', 'entry', 'image','updated_on']

    def get_queryset(self):
        return Thread.objects.filter(author__user=self.request.user)

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse_lazy('thread-detail', kwargs={'pk': self.object.pk})
