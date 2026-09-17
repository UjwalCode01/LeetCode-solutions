class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Array to store the min coins for each sub-amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, the amount cannot be formed
        return dp[amount] if dp[amount] != float('inf') else -1