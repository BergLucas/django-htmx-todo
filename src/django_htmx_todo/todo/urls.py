from django.urls import path
from django_htmx_todo.todo.views import (
    CreateTaskView,
    DeleteTaskView,
    ListTaskView,
    UpdateTaskCompletedView,
    UpdateTaskView,
)

urlpatterns = [
    path("", ListTaskView.as_view(), name="list_tasks"),
    path("<int:pk>/", DeleteTaskView.as_view(), name="delete_task"),
    path("<int:pk>/update/", UpdateTaskView.as_view(), name="update_task"),
    path(
        "<int:pk>/update/completed/",
        UpdateTaskCompletedView.as_view(),
        name="update_task_completed",
    ),
    path("create/", CreateTaskView.as_view(), name="create_task"),
]
