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
                                     related_name = 'category')
    entry = models.TextField()    
    header_image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('wiki:article_detail', args=[str(self.pk)])
        
        
    class Meta:
        ordering = ['-created_on'] # The most recent article appears first
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Comment(models.Model):
    """Class for the Comment model for the wiki app."""
    
    author = models.ForeignKey(Profile, 
                                     on_delete=models.SET_NULL, 
                                     null=True, 
                                     related_name = 'commenter')
    article = models.ForeignKey(Article, 
                                     on_delete=models.CASCADE, 
                                     null=True, 
                                     related_name = 'article')
    entry = models.TextField()    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
        
    class Meta:
        ordering = ['-created_on'] # The most recent comment appears first
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
