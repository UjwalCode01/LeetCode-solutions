class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        max_val = max(nums)
        # Total sum of each number stored in an array/map
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
            
        # House Robber DP logic
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 0
        prev1 = points[0]
        
        for i in range(1, max_val + 1):
            current = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = current
            
        return prev1