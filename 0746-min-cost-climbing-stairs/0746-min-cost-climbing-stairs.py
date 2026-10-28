class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # Iterate from the third step to the top
        for i in range(2, n):
            cost[i] += min(cost[i - 1], cost[i - 2])
        
        # The answer is the minimum cost to reach the top from either the last or second-to-last step
        return min(cost[n - 1], cost[n - 2])