from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.urls import reverse_lazy


class LoginView(DjangoLoginView):
    template_name = "login.html"
    next_page = reverse_lazy("list_tasks")

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("login")
