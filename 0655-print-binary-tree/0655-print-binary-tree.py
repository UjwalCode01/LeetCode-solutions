class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node:
                return -1
            return max(get_height(node.left), get_height(node.right)) + 1
        
        h = get_height(root)
        m = h + 1
        n = (1 << (h + 1)) - 1
        
        res = [["" for _ in range(n)] for _ in range(m)]
        
        def fill(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            
            # Only calculate offset and recurse if the node has children
            if node.left or node.right:
                offset = 1 << (h - r - 1)
                if node.left:
                    fill(node.left, r + 1, c - offset)
                if node.right:
                    fill(node.right, r + 1, c + offset)
                
        fill(root, 0, (n - 1) // 2)
        return res