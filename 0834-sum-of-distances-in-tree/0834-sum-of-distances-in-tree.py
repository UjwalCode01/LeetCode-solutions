class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Adjacency list banana
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        count = [1] * n
        ans = [0] * n
        
        # Pehla DFS: Subtree count aur root (0) ke liye initial distances calculate karne ke liye
        def dfs1(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    count[node] += count[neighbor]
                    ans[node] += ans[neighbor] + count[neighbor]
                    
        # Dusra DFS: Rerooting ke through baaki sabhi nodes ka answer nikalne ke liye
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Reroot formula: parent se child par shift hona
                    ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)
                    
        dfs1(0, -1)
        dfs2(0, -1)
        
        return ans