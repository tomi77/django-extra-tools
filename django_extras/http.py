"""
An HTTP response classes.
"""

from django.http import HttpResponse


class HttpResponseGetFile(HttpResponse):
    """
    An HTTP response class with the "download file" headers.
    """

    def __init__(self, filename, *args, **kwargs):
        super(HttpResponseGetFile, self).__init__(*args, **kwargs)
        self['Cache-Control'] = 'must-revalidate, post-check=0, pre-check=0'
        self['Content-Disposition'] = 'attachment; filename="%s"' % filename
        self['Pragma'] = 'public'
