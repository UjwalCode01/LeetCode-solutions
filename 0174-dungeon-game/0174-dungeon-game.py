class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        
        # Initialize DP table with infinity
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base condition: To stay alive after reaching past the princess, 1 HP is needed
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        # Iterate backwards from bottom-right to top-left
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                min_health_needed = min(dp[r + 1][c], dp[r][c + 1])
                dp[r][c] = max(1, min_health_needed - dungeon[r][c])
                
        return dp[0][0]