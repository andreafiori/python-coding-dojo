import math


class PrimeFactors(object):
    @staticmethod
    def get_prime_numbers(n):
        """
        Get all prime factors of a given number n
        :param n: int
        :return: list
        """
        prime_numbers = []
        # Print the number of two's that divide n
        while n % 2 == 0:
            prime_numbers.append(2),
            n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3, int(math.sqrt(n)) + 1, 2):

            # while i divides n , print i ad divide n
            while n % i == 0:
                prime_numbers.append(i)
                n = n / i

        # Condition if n is a prime, number greater than 2
        if n > 2:
            return n

        return prime_numbers

    @staticmethod
    def is_prime(num):
        """
        Check if a number is prime
        :param num: int
        :return:
        """

        # To take input from the user num = int(input("Enter a number: "))

        # prime math are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    return False
                    # print(i, "times", num // i, "is", num)
                else:
                    return True

        # if input number is less than or equal to 1, it is not prime
        else:
            return False
