"""
Wikipedia: https://en.wikipedia.org/wiki/Leap_year
"""


def is_leap(year):
    """
    Check if a year is leap
    :param year: int
    :return: bool
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            return True if (year % 400) == 0 else False
        else:
            return True
    else:
        return False
