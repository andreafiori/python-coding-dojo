"""
Binary Tree Level Order Traversal II | https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

"""

class BinaryTreeLevelOrderTraversalII:
    # import src.online.leetcode.tree_node
    # def levelOrderBottom(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root is None:
    #         return []
    #     self.get_level(res, root, 0)
    #     # reverse result
    #     res.reverse()
    #     return res

    # def get_level(self, res, root, depth):
    #     if root is None:
    #         return
    #     if depth == len(res):
    #         res.append([])
    #     res[depth].append(root.val)
    #     self.get_level(res, root.left, depth + 1)
    #     self.get_level(res, root.right, depth + 1)

    @staticmethod
    def level_order_bottom(root):
        if root is None:
            return []
        # use stack
        stack = [[root]]
        res = []
        while len(stack) > 0:
            top = stack.pop()
            res.insert(0, [t.val for t in top])
            temp = []
            for node in top:
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            if len(temp) > 0:
                stack.append(temp)
        return res
