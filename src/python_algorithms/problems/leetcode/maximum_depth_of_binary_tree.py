"""

Max depth of binary tree | leetcode 104 | https://leetcode.com/problems/maximum-depth-of-binary-tree/

given the root of a binary tree, return its maximum depth.

method: recursively increment left and right count for each new node and return max

Definition for a binary tree node.

"""

class MaximumDepthOfBinaryTree
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return 1 + max(ld, rd)

    def maxDepth(self, root):
        def findDepth(node):
            if node is None:
                return -1

            ldepth = findDepth(node.left)
            rdepth = findDepth(node.right)

            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1

        return findDepth(root) + 1