from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
            
        # Target mask when all nodes have been visited
        target_mask = (1 << n) - 1
        
        # Queue stores (node, mask, distance)
        queue = deque()
        visited = set()
        
        # We can start at any node, so push all initial states into the queue
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))
            
        while queue:
            node, mask, dist = queue.popleft()
            
            # If all nodes are visited, return the distance
            if mask == target_mask:
                return dist
                
            # Explore neighbors
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                next_state = (neighbor, next_mask)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((neighbor, next_mask, dist + 1))
                    
        return 0