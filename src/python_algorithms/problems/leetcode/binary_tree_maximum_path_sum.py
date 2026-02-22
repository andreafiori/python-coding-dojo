class Solution(object):
    def __init__(self):
        self.result = -2147483647

    def maxPathSum(self, root):
        """
        :param root:
        :return:
        """
        # return (root.val,left+root.val,right+root.val,left+right+root);
        self.get_node_max_value(root)
        return self.result

    def get_node_max_value(self, node):
        if node is None:
            return 0
        lresult = self.get_node_max_value(node.left)
        rresult = self.get_node_max_value(node.right)
        self.result = max(lresult + rresult + node.val, self.result)
        ret = node.val + max(lresult, rresult)
        # if max left or right < 0 then return 0
        if ret > 0:
            return ret
        return 0
