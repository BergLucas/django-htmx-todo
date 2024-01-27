from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django_htmx_todo.todo.components.list_tasks.list_tasks import ListTasks
from django_htmx_todo.todo.components.task_preview.task_preview import TaskPreview
from django_htmx_todo.todo.models import Task


def display_tasks(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, "display_tasks.html", {"tasks": tasks})
