from typing import Any
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from urllib.parse import urlparse

class LoginView(DjangoLoginView):
    next_page = reverse_lazy("list_tasks")

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.next_page)
        else:
            return super().get(request, *args, **kwargs)

    def get_template_names(self) -> list[str]:
        if self.request.method == "POST":
            return ["partial_login.html"]
        else:
            return ["login.html"]

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("login")

    def get_default_redirect_url(self):
        referer_header = self.request.headers.get("Referer")

        if referer_header is not None and (referer_path := urlparse(referer_header).path) != "/":
            return f"{self.next_page}?next={referer_path}"
        else:
            return super().get_default_redirect_url()
