from django.contrib import admin

# Register your models here.

from .models import Commission, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInline,]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment)