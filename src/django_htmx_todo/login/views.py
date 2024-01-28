from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django_htmx.http import HttpResponseClientRedirect

class LoginFormView(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/tasks/"

    def form_valid(self, form: AuthenticationForm) -> HttpResponseClientRedirect:
        login(self.request, form.get_user())
        return HttpResponseClientRedirect(self.get_success_url())
