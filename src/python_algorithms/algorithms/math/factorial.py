import math

"""
Factorial https://en.wikipedia.org/wiki/Factorial
Double Factorial https://en.wikipedia.org/wiki/Double_factorial
"""


class Factorial:
    @staticmethod
    def calculate(n):
        """
        Calculate factorial of a number
        :param n:
        :return:
        """
        return 1 if (n == 1 or n == 0) else n * Factorial.calculate(n - 1)

    @staticmethod
    def double_factorial(n):
        """
        Calculate double factorial
        :param n:
        :return:
        """
        return 1 if n <= 0 else n * Factorial.double_factorial(n - 2)

    # Without using recursion
    # def calculate(self, n):
    #     fact = 1
    #     for i in range(1, n + 1):
    #         fact = fact * i
    #     return fact

    @staticmethod
    def calculate_using_math(num):
        """
        Calculate Factorial
        :param num: int
        :return: int
        """
        math.factorial(num)

    @staticmethod
    def factorial_not_recursive(number):
        """
        Calculate factorial of a number with no recursion
        :param number: int
        :return: int
        """
        result = 1
        while number >= 1:
            result = result * number
            number = number - 1
        return result

    @staticmethod
    def recursive_fibonacci(index):
        if index == 0: #Base case 1
            return 0
        if index == 1: #Base case 2
            return 1
        # Every term in fib sequence = sum of previous two terms
        return  Factorial.recursive_fibonacci(index-1) + Factorial.recursive_fibonacci(index-2)
        
# print(recursive_fibonacci(0))   #0
# print(recursive_fibonacci(1))   #1
# print(recursive_fibonacci(5))   #5
# print(recursive_fibonacci(7))   #13
# print(recursive_fibonacci(10))  #55
# print(recursive_fibonacci(12))  #144
