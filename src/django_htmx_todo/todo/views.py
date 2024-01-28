from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.views.generic import View, TemplateView, UpdateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django_htmx.http import HttpResponseLocation
from django_htmx_todo.todo.models import Task
from django_htmx_todo.todo.forms import TaskForm


class ListTaskView(LoginRequiredMixin, TemplateView):
    template_name = "list_tasks.html"

    def get_context_data(self):
        tasks = Task.objects.all().order_by("pk")
        return {"tasks": tasks}


class DeleteTaskView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("list_tasks")

    def delete(self, request: HttpRequest, pk: int) -> HttpResponseLocation:
        task = get_object_or_404(self.model, pk=pk)
        task.delete()
        return HttpResponseLocation(self.success_url)


class UpdateTaskCompletedView(LoginRequiredMixin, View):
    template_name = "task_preview.html"
    model = Task
    success_url = reverse_lazy("list_tasks")

    def patch(self, request: HttpRequest, pk: int) -> HttpResponseLocation:
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return render(request, self.template_name, {"task": task})


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = "update_task.html"
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("list_tasks")
