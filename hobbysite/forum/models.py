"""This file provides the base models for the forum app."""
from django.db import models
from django.urls import reverse


class ThreadCategory(models.Model):
    """This class represents the posts' categories."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-category-detail', args=[str(self.pk)])

    class Meta:    
        """This class uses metadata from the models import to arrange
        the categories in an ascending order based on name."""

        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        

class Thread(models.Model):
    """This class represents a post, which contains categories."""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ThreadCategory, on_delete=models.SET_NULL, 
        null=True, related_name="post"
        )
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.pk)])

    class Meta:
        """This class uses metadata from the models import to arrange
        the posts in a descending order based on date created."""
        
        ordering = ['-created_on']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

class Comment(models.Model):
    "This class represents the comments that respond to a thread."
    author = models.ForeignKey(
        'user_management.models.Profile', on_delete=models.SET_NULL, 
        null=True, related_name="author"
        )
    thread = models.ForeignKey(
        Thread, on_delete=models.CASCADE, 
        null=True, related_name="thread"
        )
    entry = entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.pk)])

    class Meta:
    """This class uses metadata from the models import to arrange
    the comments in an ascending order based on date created."""

        ordering = ['created_on']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
