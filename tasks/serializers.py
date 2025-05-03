from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    
    Converts Task instances to/from JSON and validates incoming data.
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'date', 'created_at']
        read_only_fields = ['id', 'created_at']