"""
Validate binary search tree | leetcode 98 | https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

method: in-order traversal of a valid bst gives a sorted array

tip: use `prev` pointer instead of an array to keep space complexity as O(1)

"""

import sys

class ValidateBinarySearchTree:
    # initialise a prev pointer
    def __init__(self):
        self.prev = None

    def isValidBST_one(self, root):
        return self.isVaild_helper(root, -sys.maxint - 1, sys.maxint)

    def isVaild_helper(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isVaild_helper(root.left, minVal, root.val) and self.isVaild_helper(root.right, root.val, maxVal)

    # in-order traversal (L M R)
    # should return a sorted array
    def isValidBST_two(self, root) -> bool:

        # if this node is none, its a leaf
        if root is None:
            return True

        if not self.isValidBST_two(root.left):
            return False

        if self.prev is not None and self.prev.val >= root.val:
            return False

        self.prev = root

        return self.isValidBST_two(root.right)