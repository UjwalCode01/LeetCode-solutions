# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # Base Case 1: Empty tree
        if not root:
            return False
        
        # Base Case 2: Leaf node check
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Subtract current node value and recurse on children
        remainingSum = targetSum - root.val
        
        # Return True if either left or right subtree finds a valid path
        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)