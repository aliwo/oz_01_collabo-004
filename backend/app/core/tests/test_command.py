# from django.test import SimpleTestCase
# from django.db.utils import OperationalError
# from unittest.mock import patch
# from django.core.management import call_command
# from MySQLdb import OperationalError as MysqlOpError


# @patch('django.db.backends.mysql.base.DatabaseWrapper.__getitem__')
# class CommandTests(SimpleTestCase):
#     # db연결에 한번에 성공했을 때
#     def test_wait_for_db_ready(self, patched_getitem):
#         patched_getitem.return_value = True

#         call_command('wait_for_db')

#         self.assertEqual(patched_getitem.call_count, 1)

#     # db연결이 지연될 때
#     @patch('time.sleep')
#     def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
#         patched_getitem.side_effect = [MysqlOpError] \
#             + [OperationalError]*5 + [True]

#         call_command('wait_for_db')

#         self.assertEqual(patched_getitem.call_count, 7)
