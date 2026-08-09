# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        vals = []
        
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
            
        vals = [int(x) for x in data.split()]
        self.index = 0
        
        def build(lower_bound=float('-inf'), upper_bound=float('inf')):
            if self.index >= len(vals):
                return None
                
            val = vals[self.index]
            # If current value falls outside valid BST range for this subtree, return None
            if val < lower_bound or val > upper_bound:
                return None
                
            self.index += 1
            node = TreeNode(val)
            node.left = build(lower_bound, val)
            node.right = build(val, upper_bound)
            
            return node
            
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans