"""
Deepest leaves sum | leetcode 1302 | https://leetcode.com/problems/deepest-leaves-sum/
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

Example 2:
    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 19

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 100

"""

class DeepestLeavesSum:
    def solution(self, root) -> int:
        result = 0
        maxHeight = 0

        self._dfs(root, 0, result, maxHeight)
        return result

    def _dfs(self, node, currHeight, result, maxHeight):
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
        self._dfs(node.left, currHeight + 1)
        self._dfs(node.right, currHeight + 1)