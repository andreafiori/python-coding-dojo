"""
Date and time utilities
"""
class DateUtils:
    def is_leap_year(self, year):
        return self.__check_divisible_100_400(year) if (year % 4) == 0 else False

    def __check_divisible_100_400(self, year):
        if (year % 100) == 0:
            return True if (year % 400) == 0 else False
        return True
