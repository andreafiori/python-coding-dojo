#Memoization is an optimization technique used to speed up programs by storing the results of expensive function calls
#and returning the cached result when the same inputs occur again.
#In Python there's a module named functools with a method lru_cache() which allows us to use this optimization technique
#First, we'll implement memoization on our own with an example function, then with the help of lru_cache

import time, random
from functools import lru_cache

class Memoization:
    times = []
    cache = {}

    @lru_cache(maxsize=10000)
    def squaring(self, number):
        return number ** 2

    def squaring_without_memoization(self, number):
        """
        Calculate the square of a number
        """
        return number**2



    def squaring_with_memoization(self, number):
        if number in self.cache:
            return self.cache[number]
        else:
            self.cache[number] = number**2
            return self.cache[number]

# array = [random.randint(1,10) for _ in range(10000000)] #Generates an array of size 1000000 with random integers between 1-10(both included)
# t1 = time.time()
# for i in range(len(array)):
#     print(Memoization().squaring_without_memoization(array[i]))
# t2 = time.time()
# Memoization.times.append(t2-t1)

# t1 = time.time()
# for i in range(len(array)):
#     print( Memoization().squaring_with_memoization(array[i]) )
# t2 = time.time()
# Memoization.times.append(t2-t1)

# print(array)
# t1 = time.time()
# for i in range(len(array)):
#     print(squaring(array[i]))
# t2 = time.time()
# times.append(t2-t1)
#
# print(times)
# #[203.95188665390015, 148.48580384254456, 148.26833629608154]   ---  When array size was 10000000
# #[7.06306266784668, 6.145563125610352, 5.758295774459839]   ---   When array size was 1000000
#
# print(cache)
# #{8: 64, 7: 49, 6: 36, 1: 1, 4: 16, 9: 81, 2: 4, 5: 25, 3: 9, 10: 100}
#
# print(squaring.cache_info())
# #CacheInfo(hits=999990, misses=10, maxsize=10000, currsize=10)   ---   When array size was 1000000
# #CacheInfo(hits=9999990, misses=10, maxsize=10000, currsize=10)   ---  When array size was 10000000
