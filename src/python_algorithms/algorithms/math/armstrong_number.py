"""
Armstrong Number implementation

https://en.wikipedia.org/wiki/Narcissistic_number

"""


class ArmstrongNumber(object):
    def is_armstrong_number(self, num):
        # Changed num variable to string, and calculated the length (number of digits)
        order = len(str(num))

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        return num == sum

    def is_armstrong_number_three_digits(self, num):
        """
        Check if the number is an Armstrong number or not (for 3 digits)
        :param self:
        :param n:
        :return:
        """
        # take input from the user

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10

        return num == sum
