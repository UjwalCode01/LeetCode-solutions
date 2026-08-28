class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = {}
        cand1, cand2 = None, None

        # Step 1: Check for any node with two parents
        for u, v in edges:
            if v in parent:
                cand1 = [parent[v], v]  # First edge pointing to v
                cand2 = [u, v]          # Second edge pointing to v
                break
            parent[v] = u

        # Step 2: Use Union-Find to detect cycles
        dsu = list(range(n + 1))

        def find(node):
            if dsu[node] != node:
                dsu[node] = find(dsu[node])
            return dsu[node]

        for u, v in edges:
            # Skip cand2 if a node has two parents to test if removing it resolves the cycle
            if [u, v] == cand2:
                continue

            root_u = find(u)
            root_v = find(v)

            # Cycle detected
            if root_u == root_v:
                # Case 3: Two parents present, and a cycle was detected without cand2.
                # This means cand1 must be the edge forming the cycle.
                if cand1:
                    return cand1
                # Case 2: No node has two parents, cycle edge is [u, v]
                return [u, v]

            dsu[root_u] = root_v

        # Case 1: Two parents present, but no cycle detected without cand2.
        # Removing cand2 produces a valid tree.
        return cand2