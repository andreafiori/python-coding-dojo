import math


class PrimeFactors:
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


"""
python/black : True
"""

from __future__ import annotations


def prime_factors(n: int) -> list[int]:
    """
    Returns prime factors of n as a list.

    >>> prime_factors(0)
    []
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(2560)
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 5]
    >>> prime_factors(10**-2)
    []
    >>> prime_factors(0.02)
    []
    >>> x = prime_factors(10**241) # doctest: +NORMALIZE_WHITESPACE
    >>> x == [2]*241 + [5]*241
    True
    >>> prime_factors(10**-354)
    []
    >>> prime_factors('hello')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> prime_factors([1,2,'hello'])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'

    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def unique_prime_factors(n: int) -> list[int]:
    """
    Returns unique prime factors of n as a list.

    >>> unique_prime_factors(0)
    []
    >>> unique_prime_factors(100)
    [2, 5]
    >>> unique_prime_factors(2560)
    [2, 5]
    >>> unique_prime_factors(10**-2)
    []
    >>> unique_prime_factors(0.02)
    []
    >>> unique_prime_factors(10**241)
    [2, 5]
    >>> unique_prime_factors(10**-354)
    []
    >>> unique_prime_factors('hello')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> unique_prime_factors([1,2,'hello'])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'
    """
    i = 2
    factors = []
    while i * i <= n:
        if not n % i:
            while not n % i:
                n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
