"""
H index | https://leetcode.com/problems/h-index/

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:
    Input: citations = [3,0,6,1,5]
    Output: 3
    Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
    Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
    Input: citations = [1,3,1]
    Output: 1

Constraints:
    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000

"""

class Hindex:
    # def hIndex(self, citations):
    #     """
    #     :type citations: List[int]
    #     :rtype: int
    #     """
    #     # Sort and check the max h where the number of paper with no less than h citations
    #     # is no less than h
    #     citations.sort()
    #     ls = len(citations)
    #     h = ls
    #     while h > 0 and citations[ls - h] < h:
    #             h -= 1
    #     return h

    # def hIndex(self, citations):
    #     citations.sort()
    #     i = 0
    #     while i < len(citations) and citations[len(citations) - 1 - i] > i:
    #         i += 1
    #     return i

    def hIndex(self, citations):
        # counting sort
        ls = len(citations)
        papers = [0] * (ls + 1)
        for c in citations:
            papers[min(ls, c)] += 1
        k, s = ls, papers[ls]
        while k > s:
            k -= 1
            s += papers[k]
        return k
