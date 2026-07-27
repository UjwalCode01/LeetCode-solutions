class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # An empty target string 't' can always be formed 1 way (by deleting all chars in s)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for char in s:
            # Traverse backwards to use values from the previous iteration without overwriting
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]