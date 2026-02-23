"""

Binary tree zigzag level order traversal | leetcode 103 | https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

Use flag to keep track of reversed levels; O(n) because worst case is full level - n/2 elements

Definition for a binary tree node.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ZigZagConversion(object):
    def convert(self, s, numRows):
        # https://leetcode.com/discuss/90908/easy-python-o-n-solution-94%25-with-explanations
        if numRows == 1:
            return s
        # calculate period
        p = 2 * (numRows - 1)
        result = [""] * numRows
        for i in range(len(s)):
            floor = i % p
            if floor >= p//2:
                floor = p - floor
            result[floor] += s[i]
        return "".join(result)
