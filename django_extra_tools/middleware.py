from django import http
from django.conf import settings

XHR_MIDDLEWARE_ALLOWED_ORIGINS = getattr(settings, 'XHR_MIDDLEWARE_ALLOWED_ORIGINS', '*')
XHR_MIDDLEWARE_ALLOWED_METHODS = getattr(settings, 'XHR_MIDDLEWARE_ALLOWED_METHODS', ['POST', 'GET', 'OPTIONS', 'PUT',
                                                                                      'DELETE'])
XHR_MIDDLEWARE_ALLOWED_HEADERS = getattr(settings, 'XHR_MIDDLEWARE_ALLOWED_HEADERS', ['Content-Type', 'Authorization',
                                                                                      'Location', '*'])
XHR_MIDDLEWARE_ALLOWED_CREDENTIALS = getattr(settings, 'XHR_MIDDLEWARE_ALLOWED_CREDENTIALS', 'true')
XHR_MIDDLEWARE_EXPOSE_HEADERS = getattr(settings, 'XHR_MIDDLEWARE_EXPOSE_HEADERS', ['Location'])


class XhrMiddleware(object):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.

    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
    """

    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = XHR_MIDDLEWARE_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = ','.join(XHR_MIDDLEWARE_ALLOWED_METHODS)
            response['Access-Control-Allow-Headers'] = ','.join(XHR_MIDDLEWARE_ALLOWED_HEADERS)
            response['Access-Control-Allow-Credentials'] = XHR_MIDDLEWARE_ALLOWED_CREDENTIALS
            response['Access-Control-Expose-Headers'] = ','.join(XHR_MIDDLEWARE_EXPOSE_HEADERS)
            return response

        return None

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = XHR_MIDDLEWARE_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = ','.join(XHR_MIDDLEWARE_ALLOWED_METHODS)
        response['Access-Control-Allow-Headers'] = ','.join(XHR_MIDDLEWARE_ALLOWED_HEADERS)
        response['Access-Control-Allow-Credentials'] = XHR_MIDDLEWARE_ALLOWED_CREDENTIALS
        response['Access-Control-Expose-Headers'] = ','.join(XHR_MIDDLEWARE_EXPOSE_HEADERS)

        return response
