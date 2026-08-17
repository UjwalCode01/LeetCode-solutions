class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, skip)
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # If we rob this node, we must skip both children
            rob_curr = node.val + left_skip + right_skip
            
            # If we skip this node, we take the max possible from each child
            skip_curr = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_curr, skip_curr)
        
        return max(dfs(root))