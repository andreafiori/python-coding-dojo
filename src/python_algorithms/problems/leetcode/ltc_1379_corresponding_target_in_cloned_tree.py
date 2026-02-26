"""
Corresponding node in a clone of the binary tree | leetcode 1379 | https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

Return a reference to the same node in a cloned tree

Method: traverse through the original and the cloned tree parallely until the original matches the target

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CorrespondingTargetInClonedTree:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.clonedTarget = None
        def inorderTraversal(original, cloned):
            if original:
                inorderTraversal(original.left, cloned.left)
                if original is target:
                    self.clonedTarget = cloned
                inorderTraversal(original.right, cloned.right)

        inorderTraversal(original, cloned)
        return self.clonedTarget