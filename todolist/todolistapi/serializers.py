from rest_framework import serializers
from .models import Task

# Serializer for the Task model
class TaskSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # Custom date-time format

    class Meta:
        model = Task
        fields = '__all__'  # ['id', 'title', 'description', 'completed', 'created_at']