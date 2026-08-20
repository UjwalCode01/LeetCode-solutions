class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        total = 0

        # Check agar left child exist karta hai aur wo ek LEAF node hai
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        # Remaining left aur right subtrees me recursively call karo
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total