from django.contrib import admin
from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateAPIView, TaskBulkCreateUpdateAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:id>/', TaskRetrieveUpdateAPIView.as_view()),
    path('tasks/bulk/', TaskBulkCreateUpdateAPIView.as_view())
]