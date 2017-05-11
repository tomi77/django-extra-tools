import django
from django.contrib.auth.models import User


class SuperUserAuthenticateMixin(object):
    """
    Allow to login to user account through superuser login and password.
    """
    if django.VERSION[:2] < (1, 11):
        def authenticate(self, username=None, password=None):
            return self._authenticate(username=username, password=password)
    else:
        def authenticate(self, request=None, username=None, password=None):
            return self._authenticate(request=request, username=username,
                                      password=password)

    def _authenticate(self, **kwargs):
        user = super(SuperUserAuthenticateMixin, self) \
            .authenticate(**kwargs)
        if user is not None:
            return user

        username = kwargs.get('username')
        try:
            superuser_username, username = username.split(':')
        except ValueError:
            return None

        kwargs['username'] = superuser_username
        superuser = self.authenticate(**kwargs)
        if superuser is None or not superuser.is_active or \
                not superuser.is_superuser:
            return None

        return self._fetch_user(username)

    def _fetch_user(self, username):
        try:
            return User.objects.get(username=username, is_active=True)
        except User.DoesNotExist:
            return None
