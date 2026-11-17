# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        # Helper function returns a tuple of (depth, subtree_root)
        def dfs(node: TreeNode) -> tuple[int, TreeNode | None]:
            if not node:
                return 0, None
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            # If left subtree is deeper, the deepest nodes are in the left subtree
            if left_depth > right_depth:
                return left_depth + 1, left_node
            # If right subtree is deeper, the deepest nodes are in the right subtree
            elif right_depth > left_depth:
                return right_depth + 1, right_node
            # If both depths are equal, the current node is the lowest common ancestor of the deepest nodes
            else:
                return left_depth + 1, node
                
        return dfs(root)[1]