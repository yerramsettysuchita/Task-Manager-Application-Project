"""
URL configuration for task_management project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URLs from our tasks app
    path('', include('tasks.urls')),
]