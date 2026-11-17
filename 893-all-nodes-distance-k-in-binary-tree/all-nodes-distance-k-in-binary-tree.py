from collections import deque, defaultdict
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Build a parent map to convert the tree into an undirected graph
        parent_map = {}
        
        def populate_parents(node: TreeNode, parent: TreeNode = None):
            if not node:
                return
            if parent:
                parent_map[node] = parent
            populate_parents(node.left, node)
            populate_parents(node.right, node)
            
        populate_parents(root)
        
        # Step 2: Perform BFS starting from the target node
        queue = deque([target])
        visited = {target}
        current_distance = 0
        
        while queue:
            if current_distance == k:
                return [node.val for node in queue]
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # Check left neighbor
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                    
                # Check right neighbor
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                    
                # Check parent neighbor
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
                    
            current_distance += 1
            
        return []