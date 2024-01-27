from django_components import component
from django_htmx_todo.todo.models import Task


@component.register("task_preview")
class TaskPreview(component.Component):
    template_name = "task_preview/task_preview.html"

    def get_context_data(self, task: Task) -> dict:
        return {"task": task}
