"""This file sets up the models for the commissions app."""
from django.db import models
from django.urls import reverse
from datetime import datetime
from user_management.models import Profile


class Commission(models.Model):
    """Class for the Commission model for the commissions app."""

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE, 
        related_name="commision",
        null=True
        )
    description = models.TextField()

    OPEN = "A"
    FULL = "B"
    COMPLETED = "C"
    DISCONTINUED = "D"
    
    COMMISSION_STATUS_CHOICES = {
        OPEN: "Open",
        FULL: "Full",
        COMPLETED: "Completed",
        DISCONTINUED: "Discontinued",
    }

    status = models.CharField(
        max_length=50,
        choices=COMMISSION_STATUS_CHOICES, 
        default=OPEN
        )
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


class Job(models.Model):
    """Class for the Job model for the commissions app."""

    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='job'
        )
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()

    OPEN = "A"
    FULL = "B"
    
    JOB_STATUS_CHOICES = {
        OPEN: "Open",
        FULL: "Full",
    }

    status = models.CharField(
        max_length=50,
        choices=JOB_STATUS_CHOICES, 
        default=OPEN
        )
    
    def __str__(self):
        return self.role

    class Meta:
        ordering = ['status', '-manpower_required', 'role']
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

class JobApplication(models.Model):
    job = models.ForeignKey(
        Job, 
        on_delete=models.CASCADE, 
        related_name='jobapplication'
        )
    applicant = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='jobapplicant'
        )
    
    PENDING = "A"
    ACCEPTED = "B"
    REJECTED = "C"
    
    JOBAPPLICATION_STATUS_CHOICES = {
        PENDING: "Pending",
        ACCEPTED: "Accepted",
        REJECTED: "Rejected",
    }

    status = models.CharField(
        max_length=50,
        choices=JOBAPPLICATION_STATUS_CHOICES, 
        default=PENDING
        )
    applied_on = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        ordering = ['status', 'applied_on']
        verbose_name = 'job application'
        verbose_name_plural = 'job applications'
