from src.data_structures.stack import Stack

""" Numbers Utils """
class NumbersUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(number):
        temp = number
        rev = 0
        while number > 0:
            dig = number % 10
            rev = rev * 10 + dig
            number = number//10
        return True if temp == rev else False

    @staticmethod
    def factorial(number):
        result = 1
        while number >= 1:
            result = result * number
            number = number - 1
        return result

    def factorial_recursive(self, number):
        if number < 1: # base case
            return 1

        num_to_return = number * self.factorial_recursive(number - 1)  # recursive call
        # print(str(n) + '! = ' + stragr(returnNumber))
        return num_to_return

    @staticmethod
    def convert(dec_number, base):
        digits = "0123456789ABCDEF"

        remstack = Stack()

        while dec_number > 0:
            rem = dec_number % base
            remstack.push(rem)
            dec_number = dec_number // base

        new_string = ""
        while not remstack.is_empty():
            new_string = new_string + digits[remstack.pop()]

        return new_string

    @staticmethod
    def smallest_divisor(num):
        divisors = []
        for i in range(2, num + 1):
            if (num % i) == 0:
                divisors.append(i)
        divisors.sort()
        return divisors[0]

    @staticmethod
    def calculate_divisors(number):
        divisors = []
        for i in range(1, number + 1):
            if (number % i) == 0:
                divisors.append(i)
        return divisors

    @staticmethod
    def is_prime(num):
        '''check if integer number is a prime'''

        # make sure n is a positive integer
        num = abs(int(num))

        # 0 and 1 are not primes
        if num < 2:
            return False

        # 2 is the only even prime number
        if num == 2:
            return True

        # all other even numbers are not primes
        if not num & 1:
            return False

        # range starts with 3 and only needs to go up
        # the square root of nnumor all odd numbers
        for x in range(3, int(num ** 0.5) + 1, 2):
            if num % x == 0:
                return False

        return True

    @staticmethod
    def is_armstrong_number(num):
        # initialize sum
        total = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** 3
            temp //= 10

        return True if num == total else False
