class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i][j] stores the result for substring s[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single letters have length 1
        for i in range(n):
            dp[i][i] = 1
            
        # Build solution for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]