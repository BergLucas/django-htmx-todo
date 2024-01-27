from django.urls import path
from django_htmx_todo.todo.views import display_tasks, TaskPreview

urlpatterns = [
    path("", display_tasks, name="display_tasks"),
    path("<int:id>/completed/", TaskPreview.as_view(), name="set_task_completed"),
]
