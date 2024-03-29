from typing import Callable

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django_htmx.http import HttpResponseLocation


def htmx_location_middleware(
    get_response: Callable[[HttpRequest], HttpResponse]
) -> Callable[[HttpRequest], HttpResponse]:
    def middleware(request: HttpRequest) -> HttpResponse:
        response = get_response(request)
        if (
            request.htmx  # type: ignore
            and response.status_code == HttpResponseRedirect.status_code
        ):
            return HttpResponseLocation(response["location"])
        else:
            return response

    return middleware
