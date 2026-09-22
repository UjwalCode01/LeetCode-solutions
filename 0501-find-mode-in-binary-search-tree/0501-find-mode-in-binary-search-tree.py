# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.curr_val = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Process current node
            if node.val == self.curr_val:
                self.curr_count += 1
            else:
                self.curr_val = node.val
                self.curr_count = 1

            if self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.modes = [self.curr_val]
            elif self.curr_count == self.max_count:
                self.modes.append(self.curr_val)

            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.modes