from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model that provides CRUD operations.
    
    Supports:
    - Listing all tasks
    - Creating a new task
    - Retrieving a specific task
    - Updating a task
    - Deleting a task
    - Filtering by title
    - Sorting by date
    - Filtering by date
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['date']
    
    def get_queryset(self):
        """
        Override get_queryset to support custom filtering.
        
        Supported filters:
        - ?search=<title>: Search tasks by title
        - ?search_date=<date>: Filter tasks by date (YYYY-MM-DD)
        - ?sort_by_date=true: Sort tasks by date
        """
        queryset = Task.objects.all()
        
        # Search by title
        search_param = self.request.query_params.get('search', None)
        if search_param is not None:
            queryset = queryset.filter(title__icontains=search_param)
        
        # Search by date
        search_date = self.request.query_params.get('search_date', None)
        if search_date is not None:
            queryset = queryset.filter(date=search_date)
        
        # Sort by date
        sort_by_date = self.request.query_params.get('sort_by_date', None)
        if sort_by_date == 'true':
            queryset = queryset.order_by('date')
        
        return queryset