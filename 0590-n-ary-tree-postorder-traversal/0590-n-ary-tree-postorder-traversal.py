class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        
        def dfs(node):
            if not node:
                return
            # Visit all children first
            for child in node.children:
                dfs(child)
            # Append current node after processing children
            result.append(node.val)
                
        dfs(root)
        return result