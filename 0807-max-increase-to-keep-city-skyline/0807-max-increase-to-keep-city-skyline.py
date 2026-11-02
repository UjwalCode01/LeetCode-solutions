class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Har row ka maximum element calculate karein
        max_row = [max(row) for row in grid]
        
        # Har column ka maximum element calculate karein
        max_col = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        total_increase = 0
        
        # Har cell ke liye height increase sum karein
        for r in range(n):
            for c in range(n):
                total_increase += min(max_row[r], max_col[c]) - grid[r][c]
                
        return total_increase