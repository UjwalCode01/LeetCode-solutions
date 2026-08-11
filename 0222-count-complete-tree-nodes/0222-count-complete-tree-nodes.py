class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        
        # Calculate height going strictly left
        left_depth = 0
        curr = root
        while curr:
            left_depth += 1
            curr = curr.left
            
        # Calculate height going strictly right
        right_depth = 0
        curr = root
        while curr:
            right_depth += 1
            curr = curr.right
            
        # If left and right depths match, it's a perfect binary tree
        if left_depth == right_depth:
            return (1 << left_depth) - 1
            
        # Otherwise, recurse on left and right children
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)