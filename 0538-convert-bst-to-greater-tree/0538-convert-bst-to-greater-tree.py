# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.s = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # Traverse the right subtree first (larger values)
            self.convertBST(root.right)
            
            # Update the current node's value with the running sum
            self.s += root.val
            root.val = self.s
            
            # Traverse the left subtree (smaller values)
            self.convertBST(root.left)
            
        return root