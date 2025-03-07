"""This file sets up the admin panel for the wiki app."""
from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleCategoriesInline(admin.TabularInline):
     """Creates an inline for the Article model."""
    
    model = Article


class ArticleAdmin(admin.ModelAdmin):
    """Creates the admin for the ArticleCategory model."""
    
    model = ArticleCategory
    inlines = [ArticleCategoriesInline,]


admin.site.register(ArticleCategory, ArticleAdmin)
admin.site.register(Article)
