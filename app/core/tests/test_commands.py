from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTest(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # __getitem__ is used to get the db
            # mocking the behaviour of __getitem usibg patch
            gi.return_value = True
            # instead of actually retriving the db it will just return True
            call_command('wait_for_db')
            # calling the db
            self.assertEqual(gi.call_count, 1)
            # checking the mock object was called once

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        # using patch as decorator will pass as arugment to function
        # using so the test doesnt have to wait the specefied time
        # when checking to see if db will load
        """Test waiting for db, calling it 6 times"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            # will raise OperationalError 5 times
            # on the 6th time wont raise error will just return
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
