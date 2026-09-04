class Solution(object):
    def searchBST(self, root, val):
        """:type root: Optional[TreeNode] :type val: int :rtype: Optional[TreeNode]"""
        current = root
        while current and current.val != val:
            if val < current.val:
                current = current.left
            else:
                current = current.right
        return current