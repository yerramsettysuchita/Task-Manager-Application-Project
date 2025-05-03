from django.db import models
from django.utils import timezone

class Task(models.Model):
    """
    Task model representing a single to-do item.
    
    Fields:
    - title: Title of the task
    - description: Detailed description of the task
    - date: Due date of the task
    - created_at: Timestamp when the task was created
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """String representation of the task."""
        return self.title