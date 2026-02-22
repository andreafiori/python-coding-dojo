"""
Date and time utilities
"""
class DateUtils(object):
    @staticmethod
    def is_leap_year(year):
        return DateUtils.__check_divisible_100_400(year) if (year % 4) == 0 else False

    @staticmethod
    def __check_divisible_100_400(year):
        if (year % 100) == 0:
            return True if (year % 400) == 0 else False
        return True
