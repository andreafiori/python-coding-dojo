from python_algorithms.data_structures.stack import Stack


class NumbersUtil:
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
        """
        Check if integer number is a prime
        :param num: 
        :return: 
        """

        # make sure n is a positive integer
        num = abs(int(num))

        # 0 and 1 are not primes
        if num < 2:
            return False

        # 2 is the only even prime number
        if num == 2:
            return True

        # all other even math are not primes
        if not num & 1:
            return False

        # range starts with 3 and only needs to go up
        # the square root of nnumor all odd math
        for x in range(3, int(num ** 0.5) + 1, 2):
            if num % x == 0:
                return False

        return True

    @staticmethod
    def is_armstrong_number(num):
        """
        Check if num it's an Armstrong number
        :param num: int
        :return: 
        """
        total = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** 3
            temp //= 10

        return True if num == total else False
