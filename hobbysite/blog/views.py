from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Article, ArticleCategory, Comment
from .forms import ArticleCreateForm, ArticleUpdateForm, ArticleCommentForm


class ArticleListView(LoginRequiredMixin, ListView): 
    """Class for the list view of the articles"""
    model = ArticleCategory 
    template_name = 'blog_list.html' 

class ArticleDetailView(DetailView):
    """Class for the detail view of the articles"""
    model = Article 
    template_name = 'blog_detail.html'
    form_class = ArticleCommentForm
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['common_articles'] = Article.objects.filter(author=self.request.user.profile)
        ctx['comments'] = Comment.objects.all()
        ctx['comment_form'] = self.form_class()
        return ctx
    
    def form_valid(self, form):
        form.instance.article = self.get_object()
        form.instance.author = self.request.user.profile
        form.save()
        return redirect(self.request.path)

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Class for the creation of the articles"""
    model = Article
    template_name = "blog_create.html"
    form_class = ArticleCreateForm

    def form_valid(self, form):
        article = Article() # Gets the article then passes it to the instance 
        form.instance.article = article 
        form.instance.author = self.request.user.profile # Sets the author to the current user
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "blog_update.html"
    form_class = ArticleUpdateForm

    def form_valid(self, form):
        article = self.get_object() # Gets the article then passes it to the instance 
        form.instance.article = article
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)