import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution untill database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database....')
        # outputting a message to the screen
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                # try and set db_conn to the database connections
                # if connection is unavailable, will raise an OperationalError
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
        # wrapped the message in a success style that will output green output
