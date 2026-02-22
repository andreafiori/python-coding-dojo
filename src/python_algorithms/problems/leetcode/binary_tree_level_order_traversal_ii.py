class Solution(object):
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
