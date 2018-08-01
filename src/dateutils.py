""" Date and time utilities """
class DateUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def is_leap_year(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                return True if ((year % 400) == 0) else False
            else:
                return True
        else:
            return False
