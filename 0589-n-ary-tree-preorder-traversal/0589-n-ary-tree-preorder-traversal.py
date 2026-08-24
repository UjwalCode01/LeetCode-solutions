class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)
                
        dfs(root)
        return result