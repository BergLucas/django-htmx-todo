from django.forms import ModelForm
from django_htmx_todo.todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "completed"]
