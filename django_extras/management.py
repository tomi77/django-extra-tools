import atexit
import os
import sys
import tempfile

from django.core.management.base import BaseCommand


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

        filename = os.path.join(tempfile.gettempdir(), '%s.lock' % self.name)

        try:
            fd = os.open(filename, os.O_CREAT | os.O_EXCL)

            def register():
                os.close(fd)
                os.remove(filename)

            atexit.register(register)
        except OSError:
            msg = ("Script run multiple times. If this isn't true, delete "
                   "`%s`." % filename)
            sys.stderr.write(msg + "\n")
            sys.exit(1)

        self.handle_instance(*args, **options)

    def handle_instance(self, *args, **options):
        """
        Perform the command action for cron task.
        """
        raise NotImplementedError()
