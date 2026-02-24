"""
Deepest leaves sum | leetcode 1302 | https://leetcode.com/problems/deepest-leaves-sum/
"""

class deepestLeavesSum:
    def dls(self, root) -> int:
        result = 0
        maxHeight = 0

        # dfs
        def dfs(node, currHeight):
            nonlocal result, maxHeight
            if node is None:
                return

            # reset if current height is not max
            if currHeight > maxHeight:
                result = 0
                maxHeight = currHeight

            # add to sum if current height is max
            if currHeight == maxHeight:
                result += node.val

            # recursively traverse left and right subtrees
            dfs(node.left, currHeight + 1)
            dfs(node.right, currHeight + 1)

        dfs(root, 0)
        return result
