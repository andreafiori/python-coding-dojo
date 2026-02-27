"""
"""

# class TreeNode
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class InvertBinaryTree:
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # recursively
    #     if root is None:
    #         return None
    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)
    #     root.left = right
    #     root.right = left
    #     return root

    def invert(self, root):
        # iteratively
        if root is None:
            return None
        queue = [root]
        while len(queue):
            curr = queue.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return root
