# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """:type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root
        
        while curr:
            # If both p and q are greater than curr, LCA lies in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are smaller than curr, LCA lies in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Split point found (one node on left, one on right, or curr is equal to p or q)
            else:
                return curr