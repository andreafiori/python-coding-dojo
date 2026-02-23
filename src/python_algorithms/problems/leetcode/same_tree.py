"""
Same tree | leetcode 100 | https://leetcode.com/problems/same-tree/

Given a root of each of the two trees, check if the trees are the exact same or not

method: (DFS) inorder traversal to compare left subtree, current node and right subtree

"""

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q:
            return True
        try:
            left = right = True
            if p.val == q.val:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                return (left and right)
        except:
            return False
        return False

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        lResult = self.isSameTree(p.left, q.left)
        nResult = p.val == q.val
        rResult = self.isSameTree(p.right, q.right)

        return lResult and nResult and rResult