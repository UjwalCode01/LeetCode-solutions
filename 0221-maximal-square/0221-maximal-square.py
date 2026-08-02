class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # dp table initialized with 0s
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    # 1 + minimum of top, left, and top-left diagonal
                    dp[r + 1][c + 1] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r][c])
                    max_side = max(max_side, dp[r + 1][c + 1])
                    
        # Return area of the maximum square found
        return max_side * max_side