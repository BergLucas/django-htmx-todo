from django.contrib.auth.views import LoginView

class LoginFormView(LoginView):
    template_name = "login.html"
    success_url = "/tasks/"
