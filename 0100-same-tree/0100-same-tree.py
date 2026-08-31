class Solution(object):
    def isSameTree(self, p, q):
        # If both nodes are None, they are identical
        if not p and not q:
            return True
        # If one of them is None or their values don't match, they are not the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)