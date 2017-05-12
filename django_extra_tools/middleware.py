from django import http

from django_extra_tools.conf import settings


class XhrMiddleware(object):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.

    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
    """

    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = \
                settings.XHR_MIDDLEWARE_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = \
                ','.join(settings.XHR_MIDDLEWARE_ALLOWED_METHODS)
            response['Access-Control-Allow-Headers'] = \
                ','.join(settings.XHR_MIDDLEWARE_ALLOWED_HEADERS)
            response['Access-Control-Allow-Credentials'] = \
                settings.XHR_MIDDLEWARE_ALLOWED_CREDENTIALS
            response['Access-Control-Expose-Headers'] = \
                ','.join(settings.XHR_MIDDLEWARE_EXPOSE_HEADERS)

            return response

        return None

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = \
            settings.XHR_MIDDLEWARE_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = \
            ','.join(settings.XHR_MIDDLEWARE_ALLOWED_METHODS)
        response['Access-Control-Allow-Headers'] = \
            ','.join(settings.XHR_MIDDLEWARE_ALLOWED_HEADERS)
        response['Access-Control-Allow-Credentials'] = \
            settings.XHR_MIDDLEWARE_ALLOWED_CREDENTIALS
        response['Access-Control-Expose-Headers'] = \
            ','.join(settings.XHR_MIDDLEWARE_EXPOSE_HEADERS)

        return response
