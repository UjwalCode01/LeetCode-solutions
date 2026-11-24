class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v > 0:
                    area += 6 * v - 2 * (v - 1)
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            area -= min(v, grid[ni][nj])

        return area