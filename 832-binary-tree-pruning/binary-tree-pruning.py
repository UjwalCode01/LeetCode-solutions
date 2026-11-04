class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        
        # Recursively prune left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # If the current node is 0 and both its children are None, remove this node
        if root.val == 0 and not root.left and not root.right:
            return None
            
        return root