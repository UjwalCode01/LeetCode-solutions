# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_all_left(root)

    def _push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        # Top of the stack is the next smallest element
        top_node = self.stack.pop()

        # If there is a right subtree, process its left branch
        if top_node.right:
            self._push_all_left(top_node.right)

        return top_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()