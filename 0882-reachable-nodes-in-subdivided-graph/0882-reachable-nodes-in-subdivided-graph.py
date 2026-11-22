import heapq
from collections import defaultdict


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))

        dist = {0: 0}
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, float("inf")):
                continue
            for v, cost in graph[u]:
                nd = d + cost
                if nd <= maxMoves and nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        ans = len(dist)

        for u, v, cnt in edges:
            from_u = maxMoves - dist[u] if u in dist else 0
            from_v = maxMoves - dist[v] if v in dist else 0
            ans += min(cnt, from_u + from_v)

        return ans