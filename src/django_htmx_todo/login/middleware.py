from django_htmx.http import HttpResponseClientRedirect
from django.http import HttpRequest, HttpResponse


def htmx_middleware(get_response):
    def middleware(request: HttpRequest) -> HttpResponse:
        response: HttpResponse = get_response(request)
        if (request.headers.get("HX-Request") == "true" and response.status_code == 302):
            return HttpResponseClientRedirect(response["location"])
        else:
            return response

    return middleware
