import unittest
from src.data_structures.date_utils import DateUtils

class DateUtilsTest(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(DateUtils.is_leap_year(2004))
