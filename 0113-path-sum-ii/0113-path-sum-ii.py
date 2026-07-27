# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(node, currentSum, currentPath):
            if not node:
                return
            
            # Add current node value to path
            currentPath.append(node.val)
            
            # Check if it's a leaf node and path sum matches
            if not node.left and not node.right and currentSum == node.val:
                result.append(list(currentPath))  # Append a copy of currentPath
            else:
                # Recurse on left and right subtrees
                dfs(node.left, currentSum - node.val, currentPath)
                dfs(node.right, currentSum - node.val, currentPath)
            
            # Backtrack to restore state for parent call
            currentPath.pop()

        dfs(root, targetSum, [])
        return result