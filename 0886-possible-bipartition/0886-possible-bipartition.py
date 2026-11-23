from collections import deque

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        adj = [[] for _ in range(n + 1)]
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        color = [0] * (n + 1)

        for start in range(1, n + 1):
            if color[start] != 0:
                continue

            color[start] = 1
            queue = deque([start])

            while queue:
                curr = queue.popleft()
                for nxt in adj[curr]:
                    if color[nxt] == 0:
                        color[nxt] = -color[curr]
                        queue.append(nxt)
                    elif color[nxt] == color[curr]:
                        return False

        return True