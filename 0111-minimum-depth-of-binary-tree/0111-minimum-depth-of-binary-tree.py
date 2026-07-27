# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base Case 1: Empty tree
        if not root:
            return 0
        
        # Base Case 2: Leaf node (no children)
        if not root.left and not root.right:
            return 1
        
        # If left child is missing, we must go right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If right child is missing, we must go left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist, take the minimum of both paths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))