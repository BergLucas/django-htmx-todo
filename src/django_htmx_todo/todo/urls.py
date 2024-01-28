from django.urls import path
from django_htmx_todo.todo.views import TasksView, TaskPreview

urlpatterns = [
    path("", TasksView.as_view(), name="tasks_view"),
    path("<int:id>/completed/", TaskPreview.as_view(), name="set_task_completed"),
]
