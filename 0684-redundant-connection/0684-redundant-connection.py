class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = list(range(n + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            # If both nodes share the same root, this edge forms a cycle
            if root_u == root_v:
                return [u, v]

            # Union the sets
            parent[root_u] = root_v