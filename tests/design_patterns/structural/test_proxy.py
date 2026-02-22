import sys
from time import time
import unittest
from io import StringIO

from src.python_algorithms.design_patterns.structural.proxy import Proxy


class ProxyTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.p = Proxy()

    def setUp(self):
        """ Function/test case scope setup. """
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """ Function/test case scope teardown. """
        self.output.close()
        sys.stdout = self.saved_stdout

#     def test_sales_manager_shall_talk_through_proxy_with_delay(self):
#         self.p.busy = 'No'
#         start_time = time()
#         self.p.talk()
#         end_time = time()
#         execution_time = end_time - start_time
#         print_output = self.output.getvalue()
#         expected_print_output = 'Proxy checking for Sales Manager availability\n\
# Sales Manager ready to talk\n'
#         self.assertEqual(print_output, expected_print_output)
#         expected_execution_time = 1
#         self.assertEqual(int(execution_time * 10), expected_execution_time)
#
#     def test_sales_manager_shall_respond_through_proxy_with_delay(self):
#         self.p.busy = 'Yes'
#         start_time = time()
#         self.p.talk()
#         end_time = time()
#         execution_time = end_time - start_time
#         print_output = self.output.getvalue()
#         expected_print_output = 'Proxy checking for Sales Manager availability\n\
# Sales Manager is busy\n'
#         self.assertEqual(print_output, expected_print_output)
#         expected_execution_time = 1
#         self.assertEqual(int(execution_time * 10), expected_execution_time)
