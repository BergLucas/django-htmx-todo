from django.urls import path
from django_htmx_todo.todo.views import display_tasks


urlpatterns = [
    path('', display_tasks, name='display_tasks'),
]
