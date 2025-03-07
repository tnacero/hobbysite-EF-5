from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoriesInline(admin.TabularInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleCategoriesInline,]
    
admin.site.register(ArticleCategory, ArticleAdmin)
