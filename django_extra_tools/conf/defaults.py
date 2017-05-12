"""Default configuration"""

# auth.backends.SuperUserAuthenticateMixin username separator
AUTH_BACKEND_USERNAME_SEPARATOR = ':'

XHR_MIDDLEWARE_ALLOWED_ORIGINS = '*'
XHR_MIDDLEWARE_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
XHR_MIDDLEWARE_ALLOWED_HEADERS = ['Content-Type', 'Authorization', 'Location', '*']
XHR_MIDDLEWARE_ALLOWED_CREDENTIALS = 'true'
XHR_MIDDLEWARE_EXPOSE_HEADERS = ['Location']
