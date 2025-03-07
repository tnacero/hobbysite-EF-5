"""This file sets up the admin panel for the commissioins app."""
from django.contrib import admin

from .models import Commission, Comment


class CommentInline(admin.TabularInline):
    """Creates an inline for the Comment model."""

    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    """Creates the admin for the Commission model."""

    model = Commission
    inlines = [CommentInline,]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment)
