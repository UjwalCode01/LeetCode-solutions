class Solution(object):
    def findSecondMinimumValue(self, root):
        """:type root: Optional[TreeNode]
        :type: int
        """
        min1 = root.val
        self.min2 = float('inf')
        
        def dfs(node):
            if not node:
                return
            if min1 < node.val < self.min2:
                self.min2 = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return self.min2 if self.min2 != float('inf') else -1