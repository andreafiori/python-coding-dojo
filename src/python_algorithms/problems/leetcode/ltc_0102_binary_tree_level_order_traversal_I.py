"""

Binary tree level order traversal | leetcode 102 | https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Mthod: breadth first search

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

"""

class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root):
        if root is None:
            return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            if record:
                q.append(record)
        return [[x.val for x in level] for level in q]

    def levelOrder(self, root):
        res = []
        tempQ = []

        # queue to track visits
        tempQ.append(root)
        LtempQ = len(tempQ)

        # keep iterating till:
        # the track queue is empty
        while LtempQ is not 0:
            LtempQ = len(tempQ)
            level = []
            for i in range(LtempQ):
                node = tempQ.pop(0)             # pop this node from queue  (visited)
                if node is not None:
                    level.append(node.val)      # add this node to the level
                    tempQ.append(node.left)     # add left child to queue   (to visit)
                    tempQ.append(node.right)    # add right child to queue  (to visit)
            if len(level) is not 0:
                res.append(level)

        return res
