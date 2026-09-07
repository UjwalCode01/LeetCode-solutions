class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Base case: empty node or found one of the targets
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in separate subtrees, root is the LCA
        if left and right:
            return root
        
        # Otherwise, return whichever subtree found a target
        return left if left else right