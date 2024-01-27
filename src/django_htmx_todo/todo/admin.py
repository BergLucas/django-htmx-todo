from django.contrib import admin
from django_htmx_todo.todo.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed")
    list_filter = ("completed",)
    search_fields = ("title",)
