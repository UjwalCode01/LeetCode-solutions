class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        # (m+1) x (n+1) ka DP table banate hain aur 0 se fill karte hain
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases fill karte hain
        for i in range(m + 1):
            dp[i][0] = i  # Agar word2 khali hai, toh saare delete karne padenge
        for j in range(n + 1):
            dp[0][j] = j  # Agar word1 khali hai, toh saare insert karne padenge
            
        # Baaki table ko fill karte hain
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Agar characters match kar gaye
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # Agar match nahi kiye, toh 3 operations ka min lekar + 1 karenge
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],    # Insert
                        dp[i - 1][j],    # Delete
                        dp[i - 1][j - 1]  # Replace
                    )
                    
        # Bottom-right corner mein humara final answer hoga
        return dp[m][n]