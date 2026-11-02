class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

    def get_size(self, i):
        return self.size[self.find(i)]


class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        # Grid state ko modify karenge pehle saare hits apply karke
        grid_copy = [row[:] for row in grid]
        
        # Mark bricks that are hit
        for r, c in hits:
            if grid_copy[r][c] == 1:
                grid_copy[r][c] = 2  # Hit hit brick ko 2 mark kar rahe hain
            elif grid_copy[r][c] == 0:
                grid_copy[r][c] = -1 # Empty space jahan hit hua

        # Virtual top node for stability reference
        TOP = m * n
        uf = UnionFind(m * n + 1)

        def node_id(r, c):
            return r * n + c

        # Initial graph building after all hits
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == 1:
                    if r == 0:
                        uf.union(node_id(r, c), TOP)
                    if r > 0 and grid_copy[r - 1][c] == 1:
                        uf.union(node_id(r, c), node_id(r - 1, c))
                    if c > 0 and grid_copy[r][c - 1] == 1:
                        uf.union(node_id(r, c), node_id(r, c - 1))

        res = [0] * len(hits)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Reverse process of hits
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid_copy[r][c] == -1:
                continue
            
            grid_copy[r][c] = 1 # Re-add brick
            prev_roof_size = uf.get_size(TOP)
            
            # Check if this brick connects to top directly
            if r == 0:
                uf.union(node_id(r, c), TOP)

            # Union with neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid_copy[nr][nc] == 1:
                    uf.union(node_id(r, c), node_id(nr, nc))

            # New roof size after re-adding
            curr_roof_size = uf.get_size(TOP)
            
            # If addition connected new components to TOP, count fallen bricks
            if uf.find(node_id(r, c)) == uf.find(TOP):
                res[i] = max(0, curr_roof_size - prev_roof_size - 1)

        return res