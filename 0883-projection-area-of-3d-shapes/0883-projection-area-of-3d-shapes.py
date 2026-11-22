class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        xy = sum(1 for row in grid for val in row if val > 0)
        row_proj = sum(max(row) for row in grid)
        col_proj = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return xy + row_proj + col_proj