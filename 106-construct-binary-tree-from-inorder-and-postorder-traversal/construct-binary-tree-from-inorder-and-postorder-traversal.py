class Solution(object):
    def buildTree(self, inorder, postorder):
        # Create a hash map for O(1) index lookups in inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_start, in_end):
            if in_start > in_end:
                return None
            
            # The last element in current postorder range is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Get the index of the root from the inorder map
            index = inorder_map[root_val]
            
            # MUST build right subtree before left subtree 
            # because postorder yields roots in reverse (Root -> Right -> Left)
            root.right = helper(index + 1, in_end)
            root.left = helper(in_start, index - 1)
            
            return root

        return helper(0, len(inorder) - 1)