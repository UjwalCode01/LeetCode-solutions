# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            # An empty tree/node is valid
            if not node:
                return True
            
            # Current node value must be strictly within bounds
            if not (low < node.val < high):
                return False
            
            # Left child must be < node.val, Right child must be > node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Initial range is (-infinity, +infinity)
        return validate(root, float('-inf'), float('inf'))