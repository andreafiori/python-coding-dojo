"""
Leaf-Similar Trees | https://leetcode.com/problems/leaf-similar-trees/description/

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true

Example 2:
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false

Constraints:
    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LeafSimilar:
    def solution(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        leaf1 = []
        leaf2 = []
        self.dfs(root1, leaf1)
        self.dfs(root2, leaf2)
        if leaf1 == leaf2:
            return True
        return False

    def dfs(self, node, leavels):
        if not node:
            return
        if not node.left and not node.right:
            leavels.append(node.val)
        self.dfs(node.left, leavels)
        self.dfs(node.right, leavels)
