class Solution(object):
    # p.left = parent.right
    # parent.right = p.right
    # p.right = parent
    # parent = p.left
    # p = left
    def upside_down_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # top-down
        node, parent, parent_right = root, None, None
        while node is not None:
            left = node.left
            node.left = parent_right
            parent_right = node.right
            node.right = parent
            parent = node
            node = left
        return parent