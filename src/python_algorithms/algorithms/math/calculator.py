

class Calculator(object):
    @staticmethod
    def add(first, second):
        return first + second

    @staticmethod
    def subtract(first, second):
        return first - second

    @staticmethod
    def multiply(first, second):
        return first * second

    @staticmethod
    def divide(first, second):
        if second == 0:
            raise Exception("You cannot divide by zero!")
        return first / second
