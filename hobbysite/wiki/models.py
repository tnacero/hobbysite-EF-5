"""This file sets up the models for the wiki app."""
from django.db import models
from django.urls import reverse
from user_management.models import Profile

# Create your models here.

class ArticleCategory(models.Model):
    """Class for the categories of articles and their description

       name: name of the category
       description: description of the category
    """
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self): # Returns the name of a category
        return self.name
        
    def __str__(self): # Returns the description of the category
        return self.description
        
    
    class Meta:
        ordering = ['name'] # Orders the name of the categories by ascending order
        verbose_name_plural = 'categories'


class Article(models.Model):
    """Class for the specific details of the article

        title: title of the article
        author: author of the article
        category: category of the article
        entry: entry of the user in regards to the article
        header_image: image attached to the article
        created_on: date and time the article was created; automatic
        updated_on: date and time the article was last updated; automatic       
    """
    
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
    
    def __str__(self): # Returns the title of a specific article
        return self.title
        
    def get_absolute_url(self): # Returns the url of a specific article
        return reverse('wiki:article_detail', args=[str(self.pk)])
        
        
    class Meta:
        ordering = ['-created_on'] # The most recent article appears first
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Comment(models.Model):
    """Class for the specific fields found within the article

        author: author of the comment
        article: article where the comment was placed
        entry: the body of the comment
        created_on: date and time the comment was created; automatic
        updated_on: date and time the comment was last updated; automatic
    """
    
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
