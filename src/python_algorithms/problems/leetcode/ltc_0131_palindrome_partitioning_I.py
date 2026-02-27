"""
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.

"""

class PalindromePartitioning
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # https://discuss.leetcode.com/topic/6186/java-backtracking-solution/2
        result = []
        curr = []
        self.recurPartition(result, curr, s, 0)
        return result

    def recurPartition(self, result, curr, s, start):
        if start == len(s):
            result.append(list(curr))
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                curr.append(s[start:i + 1])
                self.recurPartition(result, curr, s, i + 1)
                curr.pop()

    def isPalindrome(self, s, begin, end):
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True