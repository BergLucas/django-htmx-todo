from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django_htmx_todo.todo.models import Task


def display_tasks(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, "display_tasks.html", {"tasks": tasks})
