"""This file sets up the admin panel for the commissioins app."""
from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobInline(admin.TabularInline):
    """Creates an inline for the Job model."""

    model = Job

class JobApplicationInline(admin.TabularInline):
    """Creates an inline for the JobApplication model."""

    model = JobApplication

class CommissionAdmin(admin.ModelAdmin):
    """Creates the admin for the Commission model."""

    model = Commission
    inlines = [JobInline,]

class JobAdmin(admin.ModelAdmin):
    """Creates the admin for the Job model."""

    model = Job
    inlines = [JobApplicationInline,]

class JobApplicationAdmin(admin.ModelAdmin):
    """Creates the admin for the JobApplication model."""

    model = JobApplication


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
