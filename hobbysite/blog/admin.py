from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoriesInline(admin.TabularInline):
    model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleCategoriesInline,]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)