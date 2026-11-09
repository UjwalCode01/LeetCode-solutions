class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2
        
        # Depth First Search to measure island size and label cells with island_id
        def dfs(r, c, island_id):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = island_id
            size = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                size += dfs(r + dr, c + dc, island_id)
            return size

        # Step 1: Label islands and store their sizes
        max_size = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    max_size = max(max_size, size)
                    island_id += 1

        # If the entire grid is already one big island
        if max_size == n * n:
            return n * n

        # Step 2: Evaluate flipping each 0 to 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbor_ids = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            neighbor_ids.add(grid[nr][nc])
                    
                    # Calculate new combined size (1 for the flipped cell + adjacent islands)
                    new_size = 1 + sum(island_sizes[i_id] for i_id in neighbor_ids)
                    max_size = max(max_size, new_size)

        return max_size