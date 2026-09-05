class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Append current node value to path
            current_path = path + [str(node.val)]
            
            # If it's a leaf node, join the path with "->" and add to result
            if not node.left and not node.right:
                res.append("->".join(current_path))
                return
            
            # Recurse left and right
            dfs(node.left, current_path)
            dfs(node.right, current_path)
            
        dfs(root, [])
        return res