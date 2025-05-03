from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin configuration for Task model."""
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('date',)
    date_hierarchy = 'date'