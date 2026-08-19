class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        
        # Check edge conditions
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        s1 = (total_sum + target) // 2
        
        # 1D DP array for Subset Sum
        dp = [0] * (s1 + 1)
        dp[0] = 1  # 1 way to get sum 0 (empty subset)
        
        for num in nums:
            for j in range(s1, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[s1]