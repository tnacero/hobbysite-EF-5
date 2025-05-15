"""This file sets up the admin panel for the forum app."""
from django.contrib import admin
from .models import ThreadCategory, Thread


class ThreadCategoryAdmin(admin.ModelAdmin):
    """Creates model admin for the ThreadCategory model."""

    model = ThreadCategory


class ThreadAdmin(admin.ModelAdmin):
    """Creates model admin for the Thread model."""

    model = Thread

class CommentAdmin(admin.ModelAdmin):
    """Creates model admin for the Comment model."""

    model = Comment

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
