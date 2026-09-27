# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()

        def dfs(node):
            if not node:
                return False
            
            # Check if complement exists
            if (k - node.val) in seen:
                return True
            
            # Add current node value to hash set
            seen.add(node.val)
            
            # Recurse left and right
            return dfs(node.left) or dfs(node.right)

        return dfs(root)