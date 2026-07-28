# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = [root]

        # Traverse in Root -> Right -> Left order
        while stack:
            node = stack.pop()
            res.append(node.val)

            # Push left child first so right child is popped and processed first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Reverse the result to get Left -> Right -> Root
        return res[::-1]