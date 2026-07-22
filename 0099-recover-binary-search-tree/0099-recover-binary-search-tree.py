# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Detect out-of-order nodes
            if self.prev and self.prev.val > node.val:
                # First time seeing an anomaly
                if not self.first:
                    self.first = self.prev
                # Always update second to the current node
                self.second = node

            self.prev = node

            # Traverse right subtree
            inorder(node.right)

        # 1. Find the two swapped nodes
        inorder(root)

        # 2. Swap their values in-place
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val