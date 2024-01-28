from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django_components import component
from django_htmx_todo.todo.models import Task


@component.register("task_preview")
class TaskPreview(LoginRequiredMixin, component.Component):
    template_name = "task_preview/task_preview.html"

    def get_context_data(self, task: Task) -> dict:
        return {"task": task}

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return self.render_to_response(self.get_context_data(task))