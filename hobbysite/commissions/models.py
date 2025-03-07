"""This file sets up the models for the commissions app."""
from django.db import models
from django.urls import reverse
from datetime import datetime


class Commission(models.Model):
    """Class for the Commission model for the commissions app."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:commissions-detail', args=[self.pk])

    class Meta:
        ordering = ['created_on']
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Comment(models.Model):
    """Class for the Comment model for the commissions app."""

    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='comment'
        )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
