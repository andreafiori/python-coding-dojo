"""
Binary tree paths | leetcode 257 | https://leetcode.com/problems/binary-tree-paths/

Method: (dfs) in-order traversal and at each node, update path. if leaf, append to list of paths.

"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreePath:
    def solution_one(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path):
            if root is None:
                return

            if root.left is None and root.right is None:
                path += str(root.val)
                self.paths.append(path)
                return

            path += str(root.val) + '->'
            dfs(root.left, path)
            dfs(root.right, path)

        self.paths = []
        dfs(root, "")

        return self.paths

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        paths = []
        self.get_path(paths, [], root)
        res = ['->'.join(p) for p in paths ]
        return res

    def get_path(self, result, path, node):
        if node.left is None and node.right is None:
            result.append(path + [str(node.val)])
            return
        path = path + [str(node.val)]
        if node.left is not None:
            self.get_path(result, path, node.left)
        if node.right is not None:
            self.get_path(result, path, node.right)
