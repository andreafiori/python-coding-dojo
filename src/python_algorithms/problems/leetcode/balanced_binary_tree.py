"""
Definition for a binary tree node.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
    Given the following tree [3,9,20,null,null,15,7]:

        3
       / \
      9  20
      /   \
     15   7
    Return true.

Example 2:
    Given the following tree [1,2,2,3,3,null,null,4,4]:

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.

"""
class BalancedBinaryTree(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Bottom-up recursion with sentinel -1
        if root is None:
            return True
        if self.getDepth(root) < 0:
            return False
        return True
    
    def getDepth(self, node):
        """
        Get Depth
        :param node:
        :return:
        """
        if node is None:
            return 1
        ld = self.getDepth(node.left)
        if ld < 0:
            return -1
        rd = self.getDepth(node.right)
        if rd < 0:
            return -1
        elif abs(ld - rd) > 1:
            return -1
        else:
            return max(ld, rd) + 1

    # https://discuss.leetcode.com/topic/7798/the-bottom-up-o-n-solution-would-be-better
    # def isBalanced(self, root):
    #     # Top-down recursion
    #     if root is None:
    #         return True
    #     left = self.depth(root.left)
    #     right = self.depth(root.right)
    #     return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # def depth(self, root):
    #     if root is None:
    #         return 0
    #     return max(self.depth(root.left), self.depth(root.right)) + 1
