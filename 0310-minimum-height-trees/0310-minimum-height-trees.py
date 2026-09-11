from collections import defaultdict, deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Edge cases: 0 or 1 node
        if n <= 2:
            return [i for i in range(n)]

        # Build adjacency list and track degree of each node
        neighbors = defaultdict(set)
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        # Initialize leaves queue
        leaves = deque([i for i in range(n) if len(neighbors[i]) == 1])

        # Trim leaves until <= 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # Get the only neighbor of the current leaf
                neighbor = neighbors[leaf].pop()
                # Remove edge from neighbor's set
                neighbors[neighbor].remove(leaf)

                # If neighbor becomes a new leaf, add it
                if len(neighbors[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)