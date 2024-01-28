from django.urls import path
from django_htmx_todo.login.views import LoginFormView

urlpatterns = [
    path("login/", LoginFormView.as_view(), name="login_form"),
]
