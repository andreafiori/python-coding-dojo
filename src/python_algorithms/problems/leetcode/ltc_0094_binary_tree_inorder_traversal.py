"""
Binary tree inorder traversal | https://leetcode.com/problems/binary-tree-inorder-traversal/

Method: left subtree, node, right subtree recursively

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    Output: [4,2,6,5,7,1,3,9,8]

Example 3:
    Input: root = []
    Output: []

Example 4:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def in_order_traversal(root):
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            if curr.right is not None:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
        return res

    def inorderTraversal(self, root):
        travList = []

        def traverse(root, travList):
            if root is None:
                return None

            traverse(root.left, travList)       # traverse left subtree and add nodes
            travList.append(root.val)           # add this node
            traverse(root.right, travList)      # traverse right subtree and add nodes

        traverse(root, travList)
        return travList