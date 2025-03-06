from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, 
                                    on_delete=models.CASCADE,
                                    related_name='category')
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title) 
    
    def get_absolute_url(self):
        return reverse("blog:article-detail", args=[self.pk])
    
    class Meta:
        ordering = ['-created_on']
# Create your models here.
