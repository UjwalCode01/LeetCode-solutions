class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
            
        def build_trees(start, end):
            if start > end:
                return [None]
                
            all_trees = []
            for i in range(start, end + 1):
                # Left subtrees generate karo
                left_trees = build_trees(start, i - 1)
                # Right subtrees generate karo
                right_trees = build_trees(i + 1, end)
                
                # Sabhi combinations ko root ke sath jodo
                for l in left_trees:
                    for r in right_trees:
                        current_root = TreeNode(i)
                        current_root.left = l
                        current_root.right = r
                        all_trees.append(current_root)
                        
            return all_trees

        return build_trees(1, n)