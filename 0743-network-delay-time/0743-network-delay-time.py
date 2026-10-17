import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        # Step 2: Min-heap stores tuples of (current_time, node)
        min_heap = [(0, k)]
        distances = {}
        
        # Step 3: Dijkstra's algorithm traversal
        while min_heap:
            time, u = heapq.heappop(min_heap)
            
            if u in distances:
                continue
            distances[u] = time
            
            for v, w in adj[u]:
                if v not in distances:
                    heapq.heappush(min_heap, (time + w, v))
                    
        # Step 4: Check if all nodes received the signal
        if len(distances) != n:
            return -1
            
        # The answer is the maximum time it took to reach any node
        return max(distances.values())