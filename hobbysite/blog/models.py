from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    ordering = ['category']
    
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, 
                                    on_delete=models.SET_NULL,
                                    related_name='category')
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(null=False)
    updated_on = models.DateTimeField(null=False)
    #Work on: Order of categories must be in descending order

# Create your models here.
