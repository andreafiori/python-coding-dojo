"""
Minimum absolute difference in BST | leetcode 530 | https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Method: dfs, inorder traversal

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode):
        minDiff = float('inf')
        prevNod = None

        def dfs(node):
            nonlocal minDiff, prevNod
            if node is None:
                return

            dfs(node.left)

            if prevNod != None:
                minDiff = min(minDiff, abs(node.val - prevNod))
            prevNod = node.val

            dfs(node.right)

        dfs(root)
        return minDiff


