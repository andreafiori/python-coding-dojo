"""
Invert a binary tree. | https://leetcode.com/problems/invert-binary-tree/

Method: (dfs) keep recursively swapping left and right subtrees

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InvertBinaryTree:
    def invertTree(self, root):
        self._dfs(root)
        return root

    def _dfs(self, root):
            if root is None:
                return

            if root.left is None and root.right is None:
                return

            root.left, root.right = root.right, root.left

            self._dfs(root.left)
            self._dfs(root.right)
