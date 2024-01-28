from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django_htmx_todo.todo.components.list_tasks.list_tasks import ListTasks
from django_htmx_todo.todo.components.task_preview.task_preview import TaskPreview
from django_htmx_todo.todo.models import Task


class TasksView(LoginRequiredMixin, TemplateView):
    template_name = "display_tasks.html"

    def get_context_data(self):
        tasks = Task.objects.all()
        return {"tasks": tasks}
