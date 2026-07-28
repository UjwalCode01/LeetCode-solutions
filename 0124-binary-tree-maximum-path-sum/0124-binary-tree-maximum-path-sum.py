# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Ignore subtrees with negative path sums by taking max with 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Max path sum with current node as the highest point (curve)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global max sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max path sum if continuing up to parent node
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum