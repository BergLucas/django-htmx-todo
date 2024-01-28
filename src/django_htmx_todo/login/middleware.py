from django_htmx.http import HttpResponseLocation
from django.http import HttpRequest, HttpResponse
from typing import Callable

def htmx_middleware(get_response: Callable[[HttpRequest], HttpResponse]) -> Callable[[HttpRequest], HttpResponse]:
    def middleware(request: HttpRequest) -> HttpResponse:
        response = get_response(request)
        if (request.headers.get("HX-Request") == "true" and response.status_code == 302):
            return HttpResponseLocation(response["location"])
        else:
            return response

    return middleware
