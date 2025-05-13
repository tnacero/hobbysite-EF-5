"""This file sets up the models for the wiki app."""
from django.db import models
from django.urls import reverse
from user_management.models import Profile

# Create your models here.

class ArticleCategory(models.Model):
    """Class for the ArticleCategory model for the wiki app."""
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
        
    def __str__(self):
        return self.description
        
    
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Article(models.Model):
    """Class for the Article model for the wiki app."""
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, 
                                     on_delete=models.SET_NULL, 
                                     null=True, 
                                     related_name = 'author')
    category = models.ForeignKey(ArticleCategory, 
                                     on_delete=models.SET_NULL, 
                                     null=True, 
                                     related_name = 'article')
    entry = models.TextField()    
    header_image = models.ImageField(upload_to='static/img/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
    def __str__(self):
        return self.category
    
    def __str__(self):
        return self.created_on
    
    def __str__(self):
        return self.updated_on
        
    def get_absolute_url(self):
        return reverse('wiki:article-detail', args=[str(self.pk)])
        
        
    class Meta:
        ordering = ['-created_on'] 
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Comment(models.Model):
    """Class for the Comment model for the wiki app."""
    
    author = models.ForeignKey(Profile, 
                                     on_delete=models.SET_NULL, 
                                     null=True, 
                                     related_name = 'author')
    article = models.ForeignKey(Article, 
                                     on_delete=models.CASCADE, 
                                     null=True, 
                                     related_name = 'article')
    entry = models.TextField()    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author
        
    def __str__(self):
        return self.article
    
    def __str__(self):
        return self.created_on
    
    def __str__(self):
        return self.updated_on
        
    def get_absolute_url(self):
        return reverse('wiki:article-detail', args=[str(self.pk)])
        
        
    class Meta:
        ordering = ['created_on'] 
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
