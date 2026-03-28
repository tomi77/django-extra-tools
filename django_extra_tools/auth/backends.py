from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from django_extra_tools.conf import settings


class ThroughSuperuserModelBackend(ModelBackend):
    """
    Allow to login to user account through superuser login and password.
    """
    def authenticate(self, request=None, username=None, password=None):
        return self._authenticate(request=request, username=username,
                                  password=password)

    def _authenticate(self, **kwargs):
        username = kwargs.get('username')
        try:
            separator = settings.AUTH_BACKEND_USERNAME_SEPARATOR
            superuser_username, username = username.split(separator)
        except ValueError:
            return None

        kwargs['username'] = superuser_username
        superuser = super().authenticate(**kwargs)

        if superuser is None or not superuser.is_superuser:
            return None

        try:
            user = User.objects.get(username=username)
            return user if self.user_can_authenticate(user) else None
        except User.DoesNotExist:
            return None
