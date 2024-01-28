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

    def get_redirect_url(self):
        referer_header = self.request.headers.get("Referer")
        redirect_url = super().get_redirect_url()

        if not redirect_url and referer_header is not None:
            return urlparse(referer_header).path
        else:
            return redirect_url
