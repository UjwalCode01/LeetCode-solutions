class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[members][profit]
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for g, p in zip(group, profit):
            # Reverse loops taaki ek crime ek hi baar use ho
            for members in range(n - g, -1, -1):
                for curr_profit in range(minProfit, -1, -1):
                    new_profit = min(minProfit, curr_profit + p)
                    dp[members + g][new_profit] = (dp[members + g][new_profit] + dp[members][curr_profit]) % MOD
                    
        # Sabhi valid member counts (0 to n) jinka profit minProfit tak pahuncha ho
        return sum(dp[i][minProfit] for i in range(n + 1)) % MOD