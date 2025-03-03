from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission-detail', args=[self.pk])
    
    class Meta:
        ordering = ['created_on'] 
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='commission'
        )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['-created_on'] 
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    