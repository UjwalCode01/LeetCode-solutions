class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize dp array with maximum possible counts
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute squares that are <= n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        
        for i in range(1, n + 1):
            for sq in squares:
                if i < sq:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
                
        return dp[n]