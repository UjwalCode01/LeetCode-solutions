from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        @lru_cache(None)
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            
            # Base cases: out of bounds ya thorn (-1)
            if (r1 == n or c1 == n or r2 == n or c2 == n or 
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return -float('inf')
                
            # Agar dono destination (n-1, n-1) par pahunch gaye
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
                
            # Current positions par cherries collect karein
            cherries = 0
            if r1 == r2 and c1 == c2:
                cherries += grid[r1][c1]
            else:
                cherries += grid[r1][c1] + grid[r2][c2]
                
            # 4 possible moves try karein dono ke liye:
            # (Down, Down), (Down, Right), (Right, Down), (Right, Right)
            res = max(
                dp(r1 + 1, c1, r2 + 1),     # Down, Down
                dp(r1 + 1, c1, r2),         # Down, Right
                dp(r1, c1 + 1, r2 + 1),     # Right, Down
                dp(r1, c1 + 1, r2)          # Right, Right
            )
            
            return cherries + res

        ans = dp(0, 0, 0)
        return max(0, ans)