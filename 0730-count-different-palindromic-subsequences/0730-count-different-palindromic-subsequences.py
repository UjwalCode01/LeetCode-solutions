class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # Precompute previous and next occurrences for each character ('a', 'b', 'c', 'd')
        prev_pos = [[-1] * n for _ in range(4)]
        next_pos = [[n] * n for _ in range(4)]
        
        last = [-1] * 4
        for i in range(n):
            c = ord(s[i]) - ord('a')
            for ch in range(4):
                prev_pos[ch][i] = last[ch]
            last[c] = i
            
        nxt = [n] * 4
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')
            for ch in range(4):
                next_pos[ch][i] = nxt[ch]
            nxt[c] = i
            
        # dp[i][j] stores the number of different palindromic subsequences in s[i...j]
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD
                else:
                    c = ord(s[i]) - ord('a')
                    low = next_pos[c][i]
                    high = prev_pos[c][j]
                    
                    if low > high:
                        # Characters s[i] and s[j] appear only at the endpoints
                        dp[i][j] = (2 * dp[i+1][j-1] + 2) % MOD
                    elif low == high:
                        # Character appears exactly once in between
                        dp[i][j] = (2 * dp[i+1][j-1] + 1) % MOD
                    else:
                        # Character appears two or more times in between
                        dp[i][j] = (2 * dp[i+1][j-1] - dp[low+1][high-1]) % MOD
                        
                dp[i][j] = (dp[i][j] + MOD) % MOD
                
        return dp[0][n-1]