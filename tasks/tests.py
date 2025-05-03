from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task
import datetime

class TaskAPITests(TestCase):
    """
    Test suite for the Task API.
    
    Tests CRUD operations and filtering capabilities.
    """
    
    def setUp(self):
        """Set up test data and client."""
        self.client = APIClient()
        
        # Create test tasks
        Task.objects.create(
            title="Test Task 1",
            description="Description for test task 1",
            date=datetime.date(2023, 1, 1)
        )
        Task.objects.create(
            title="Test Task 2",
            description="Description for test task 2",
            date=datetime.date(2023, 2, 1)
        )
    
    def test_list_tasks(self):
        """Test retrieving all tasks."""
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_create_task(self):
        """Test creating a new task."""
        url = reverse('task-list')
        data = {
            'title': 'New Test Task',
            'description': 'Description for new test task',
            'date': '2023-03-01'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
    
    def test_retrieve_task(self):
        """Test retrieving a specific task."""
        task = Task.objects.first()
        url = reverse('task-detail', args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task.title)
    
    def test_update_task(self):
        """Test updating a task."""
        task = Task.objects.first()
        url = reverse('task-detail', args=[task.id])
        data = {
            'title': 'Updated Task Title',
            'description': task.description,
            'date': task.date
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task Title')
    
    def test_delete_task(self):
        """Test deleting a task."""
        task = Task.objects.first()
        url = reverse('task-detail', args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
    
    def test_search_by_title(self):
        """Test searching tasks by title."""
        url = reverse('task-list') + '?search=Test Task 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Task 1')
    
    def test_search_by_date(self):
        """Test filtering tasks by date."""
        url = reverse('task-list') + '?search_date=2023-01-01'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Task 1')
    
    def test_sort_by_date(self):
        """Test sorting tasks by date."""
        url = reverse('task-list') + '?sort_by_date=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Test Task 1')
        self.assertEqual(response.data['results'][1]['title'], 'Test Task 2')