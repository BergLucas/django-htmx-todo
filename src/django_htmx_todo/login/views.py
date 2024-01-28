from typing import Any
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

class LoginView(DjangoLoginView):
    template_name = "login.html"
    next_page = reverse_lazy("list_tasks")

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.next_page)
        else:
            return super().get(request, *args, **kwargs)

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("login")
