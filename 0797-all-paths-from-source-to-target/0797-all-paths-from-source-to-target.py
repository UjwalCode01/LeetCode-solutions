class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        result = []
        
        def dfs(curr_node, path):
            if curr_node == target:
                result.append(list(path))
                return
            
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop() # Backtrack
                
        dfs(0, [0])
        return result