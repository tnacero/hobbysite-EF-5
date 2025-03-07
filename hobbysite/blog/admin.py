from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoriesInline(admin.TabularInline): # Makes it possible to update Article via the admin panel
    """Class for allowing addition and updating of Article objects via the admin panel"""
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    """Class for allowing the addition and updating of ArticleCategory objects via the admin panel"""
    model = ArticleCategory
    inlines = [ArticleCategoriesInline,]
    
admin.site.register(ArticleCategory, ArticleAdmin) 
admin.site.register(Article) 