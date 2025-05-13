from django.db import models
from django.urls import reverse


class ThreadCategory(models.Model):
    """This class represents the thread's categories."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-category-detail', args=[str(self.pk)])

    class Meta:
    """This class uses metadata from the models import to arrange"""
    """the categories in an ascending order based on name."""

        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        

class Thread(models.Model):
    """This class represents a thread, which contains categories."""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ThreadCategory, on_delete=models.SET_NULL, 
        null=True, related_name="thread"
        )
        entry = models.TextField(blank=False)
        created_on = models.DateTimeField(auto_now_add=True, null=False)
        updated_on = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.pk)])

    class Meta:
    """This class uses metadata from the models import to arrange"""
    """the threads in a descending order based on date created."""
    
        ordering = ['-created_on']
        verbose_name = 'thread'
        verbose_name_plural = 'threads'
