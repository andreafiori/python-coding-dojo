"""
Fibonacci math
"""
class Fibonacci:
    def calculate(self, n):
        """
        Function for nth Fibonacci number
        :param n: int
        :return:
        """
        if n < 0:
            raise Exception("Invalid input")
            # First Fibonacci number is 0
        elif n == 1:
            return 0
            # Second Fibonacci number is 1
        elif n == 2:
            return 1
        else:
            return self.calculate(n - 1) + self.calculate(n - 2)

        #Given a number, we have to return the number at that index of the fibonacci sequence.
        #Fibonacci Sequence - 0 1 1 2 3 5 8 13 21 34 55 89 144 . . . .
        #For example, fibonacci(5) should return 5 as the 5th index (staring from 0) of the fibonacci sequence is the number 5
        #Again , we will do both the iterative and recursive solutions

    def iterative_fibonacci(self, index):
        first_number = 0
        second_number = 1
        if index == 0:
            return first_number
        if index == 1:
            return second_number
        for i in range(2,index +1):
            third_number = first_number + second_number
            first_number = second_number
            second_number = third_number
        return third_number

    def recursive_fibonacci(self, index):
        if index == 0: #Base case 1
            return 0
        if index == 1: #Base case 2
            return 1
        #Every term in fib sequence = sum of previous two terms
        return self.recursive_fibonacci(index-1) + self.recursive_fibonacci(index-2)

# print(iterative_fibonacci(0))  #0
# print(iterative_fibonacci(1))  #1
# print(iterative_fibonacci(5))  #5
# print(iterative_fibonacci(7))  #13
# print(iterative_fibonacci(10)) #55
# print(iterative_fibonacci(12)) #144

# print(recursive_fibonacci(0))   #0
# print(recursive_fibonacci(1))   #1
# print(recursive_fibonacci(5))   #5
# print(recursive_fibonacci(7))   #13
# print(recursive_fibonacci(10))  #55
# print(recursive_fibonacci(12))  #144
