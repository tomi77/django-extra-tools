import sys

from django.core.management.base import BaseCommand

from django_extra_tools.lockers import LockError, lock


class OneInstanceCommand(BaseCommand):
    """
    A management command which will be run only one instance of command with
    name ``name``. No other command with name ``name`` can not be run in the
    same time.

    Rather than implementing ``handle()``, subclasses must implement
    ``handle_instance()``, which will be called when no other command
    with name ``name`` will be running.
    """
    name = None

    def handle(self, *args, **options):
        if self.name is None:
            raise NotImplemented('set name parameter')

        try:
            lock(self.name)
        except LockError as exc:
            self.lock_error_handler(exc)

        self.handle_instance(*args, **options)

    def handle_instance(self, *args, **options):
        """
        Perform the command action for cron task.
        """
        raise NotImplementedError()

    def lock_error_handler(self, exc):
        """
        Perform the action for lock error.
        """
        sys.stderr.write("%s\n" % exc)
        sys.exit(1)


class NagiosCheckCommand(BaseCommand):
    """
    A management command which perform a Nagios check.

    Rather than implementing ``handle()``, subclasses must implement
    ``handle_nagios_check()``, which will return a tuple `status`, `msg`.
    """
    STATE_OK = 0
    STATE_WARNING = 1
    STATE_CRITICAL = 2
    STATE_UNKNOWN = 3
    STATE_DEPENDENT = 4

    def handle(self, *args, **options):
        status, msg = self.handle_nagios_check(*args, **options)

        if not msg.endswith('\n'):
            msg = '%s\n' % msg
        self.stdout.write(msg)
        sys.exit(status)

    def handle_nagios_check(self, *args, **options):
        """
        Perform the command action for Nagios check.
        """
        raise NotImplementedError()
