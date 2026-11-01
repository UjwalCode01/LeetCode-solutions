class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = str(root.val)
        
        # If there is a left child, or if there's no left child but there is a right child
        # we need to include parentheses for the left side (which might be empty like "()")
        if root.left or root.right:
            res += "(" + self.tree2str(root.left) + ")"
            
        # Right child is only added if it actually exists
        if root.right:
            res += "(" + self.tree2str(root.right) + ")"
            
        return res