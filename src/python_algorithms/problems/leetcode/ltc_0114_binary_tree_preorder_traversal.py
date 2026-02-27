"""
Binary tree preorder traversal | leetcode 94 | https://leetcode.com/problems/binary-tree-preorder-traversal/
method: node, left subtree, right subtree recursively

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreePreordertraversal:
    def inorderTraversal(self, root: TreeNode):
        travList = []
        self.traverse(root, travList)
        return travList

    # Traverse right subtree and add nodes
    def traverse(self,root, travList):
        if root is None:
            return None

        # Add this node
        travList.append(root.val)
        # traverse left subtree and add nodes
        self.traverse(root.left, travList)
        self.traverse(root.right, travList)
