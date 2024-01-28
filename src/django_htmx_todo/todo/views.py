from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from django.shortcuts import get_object_or_404
from django_htmx_todo.todo.components.task_preview.task_preview import TaskPreview
from django_htmx_todo.todo.models import Task
from django_htmx_todo.todo.forms import TaskForm
from django_htmx.http import HttpResponseClientRedirect


class ListTaskView(LoginRequiredMixin, TemplateView):
    template_name = "list_tasks.html"

    def get_context_data(self):
        tasks = Task.objects.all().order_by("pk")
        return {"tasks": tasks}


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = "update_task.html"
    form_class = TaskForm
    model = Task
    success_url = "/tasks/"
