class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        # 0: Unvisited, 1: Visiting (currently in DFS path), 2: Safe (visited & safe)
        state = [0] * n

        def dfs(node):
            if state[node] > 0:
                # Agar node 2 (safe) hai toh True, agar 1 (cycle in path) hai toh False
                return state[node] == 2
            
            # Marking as visiting
            state[node] = 1
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            # Agar sare neighbors safe hain, toh current node bhi safe hai
            state[node] = 2
            return True

        safe_nodes = []
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
                
        return safe_nodes