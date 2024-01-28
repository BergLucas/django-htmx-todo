from django.urls import path
from django_htmx_todo.todo.views import ListTaskView, UpdateTaskView, TaskPreview

urlpatterns = [
    path("", ListTaskView.as_view(), name="tasks_view"),
    path("<int:pk>/completed/", TaskPreview.as_view(), name="update_task_completed"),
    path("<int:pk>/update/", UpdateTaskView.as_view(), name="update_task"),
]
