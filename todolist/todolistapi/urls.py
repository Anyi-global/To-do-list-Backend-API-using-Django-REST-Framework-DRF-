from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView

# URL patterns for the to-do list API
urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task-detail'),
]