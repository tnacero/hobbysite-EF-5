"""This file sets up the admin panel for the forum app."""
from django.contrib import admin
from .models import PostCategory, Post


class PostCategoryAdmin(admin.ModelAdmin):
    """Creates model admin for the PostCategory model."""

    model = PostCategory


class PostAdmin(admin.ModelAdmin):
    """Creates model admin for the Post model."""

    model = Post

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
