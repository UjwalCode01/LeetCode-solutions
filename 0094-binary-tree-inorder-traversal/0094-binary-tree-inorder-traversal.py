class Solution(object):
    def inorderTraversal(self, root):
        res = []
        
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
            
        helper(root)
        return res