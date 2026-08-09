from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        
        # Build the directed weighted graph
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1.0
            if src == target:
                return 1.0
                
            queue = deque([(src, 1.0)])
            visited = {src}
            
            while queue:
                curr, curr_product = queue.popleft()
                
                if curr == target:
                    return curr_product
                    
                for neighbor, weight in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_product * weight))
                        
            return -1.0

        return [bfs(q[0], q[1]) for q in queries]