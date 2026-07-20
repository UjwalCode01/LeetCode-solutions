class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # 1. Pehli Row ko update karo (sirf left se right ja sakte hain)
        for c in range(1, n):
            grid[0][c] += grid[0][c-1]
            
        # 2. Pehle Column ko update karo (sirf upar se neeche aa sakte hain)
        for r in range(1, m):
            grid[r][0] += grid[r-1][0]
            
        # 3. Baaki pure grid ke liye minimum cost rasta chuno
        for r in range(1, m):
            for c in range(1, n):
                # Current cell + min(Top cell, Left cell)
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                
        # Bottom-right corner mein sabse chota path sum mil jayega
        return grid[m-1][n-1]