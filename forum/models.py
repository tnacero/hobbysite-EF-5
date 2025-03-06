"""This file provides the base models for the forum app."""
from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    """This class represents the posts' categories."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
    """This class uses metadata from the models import to arrange"""
    """the categories in an ascending order based on name."""

        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        

class Post(models.Model):
    """This class represents a post, which contains categories."""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, 
        null=True, related_name="post"
        )
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_category_detail', args=[str(self.pk)])

    class Meta:
    """This class uses metadata from the models import to arrange"""
    """the posts in a descending order based on date created."""
    
        ordering = ['-created_on']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
