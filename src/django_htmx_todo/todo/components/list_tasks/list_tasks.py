from django.db.models.query import QuerySet
from django_components import component
from django_htmx_todo.todo.models import Task


@component.register("list_tasks")
class ListTasks(component.Component):
    template_name = "list_tasks/list_tasks.html"

    def get_context_data(self, tasks: QuerySet[Task]) -> dict:
        return {"tasks": tasks}
