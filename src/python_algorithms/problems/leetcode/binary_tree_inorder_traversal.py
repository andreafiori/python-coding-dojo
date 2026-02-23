"""

Binary tree inorder traversal | leetcode 94 | https://leetcode.com/problems/binary-tree-inorder-traversal/
Method: left subtree, node, right subtree recursively

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
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