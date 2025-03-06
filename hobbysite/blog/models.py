from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    ordering = ['category']
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse("blog:category", args=[self.pk])
    
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
