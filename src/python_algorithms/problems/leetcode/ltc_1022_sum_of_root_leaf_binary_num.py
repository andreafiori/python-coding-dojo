"""
Sum of root to leaf binary numbers | leetcode 1022 | https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
method: (dfs) for each node, left-shift 1 bit and add val.
        return sum of both left and right subtree
        return sum till now at each leaf
"""

class SumRootToLeafBinary:
    def sumRootToLeaf(self, root) -> int:
        def dfsSum(root, total):
            if root is None:
                return 0

            total = (total << 1) | root.val

            if root.left is None and root.right is None:
                return total

            return dfsSum(root.left, total) + dfsSum(root.right, total)

        return dfsSum(root, 0)
