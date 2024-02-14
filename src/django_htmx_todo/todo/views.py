from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, View
from django_htmx.http import HttpResponseLocation
from django_htmx_todo.todo.forms import TaskForm
from django_htmx_todo.todo.models import Task


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

    def patch(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return render(request, self.template_name, {"task": task})


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("list_tasks")

    def get_template_names(self) -> list[str]:
        if self.request.method == "POST":
            return ["partial_update_task.html"]
        else:
            return ["update_task.html"]


class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("list_tasks")

    def get_template_names(self) -> list[str]:
        if self.request.method == "POST":
            return ["partial_create_task.html"]
        else:
            return ["create_task.html"]

    def form_valid(self, form: TaskForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
