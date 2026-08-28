# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_len = 0

        def dfs(node):
            if not node:
                return 0

            # Compute longest univalue paths for left and right subtrees
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_path = 0
            right_path = 0

            # Extend path if child's value matches current node's value
            if node.left and node.left.val == node.val:
                left_path = left_len + 1

            if node.right and node.right.val == node.val:
                right_path = right_len + 1

            # Combined path through the current node
            self.max_len = max(self.max_len, left_path + right_path)

            # Return max single-direction path extending to parent
            return max(left_path, right_path)

        dfs(root)
        return self.max_len