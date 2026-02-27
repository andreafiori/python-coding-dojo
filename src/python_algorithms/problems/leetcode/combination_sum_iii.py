import itertools as it


class Solution:

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return list( it.filter(lambda x: sum(x) == n, list(it.combinations(range(1, 10), k))) )
