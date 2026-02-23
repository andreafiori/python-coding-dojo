"""
Symmetric tree | leetcode 101 | https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself

Method: recursively compare two copies of the same tree

"""

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirrorVisit(root.left, root.right)

    def isSymmetric_two(self, root):
        def checkSymm(copy1, copy2):
            if copy1 is None and copy2 is None:
                return True
            if copy1 is None or copy2 is None:
                return False

            return (copy1.val == copy2.val) and checkSymm(copy1.left, copy2.right) and checkSymm(copy1.right, copy2.left)

        return checkSymm(root, root)

    def mirrorVisit(self, left, right):
        if left is None and right is None:
            return True
        try:
            if left.val == right.val:
                if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
                    return True
            return False
        except:
            return False