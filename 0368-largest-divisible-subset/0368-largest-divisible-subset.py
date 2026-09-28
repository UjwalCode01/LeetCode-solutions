class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[List[int]] -> List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        
        dp = [1] * n
        prev = [-1] * n
        
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > dp[max_idx]:
                max_idx = i
                
        # Backtrack to reconstruct the subset
        result = []
        curr = max_idx
        while curr != -1:
            result.append(nums[curr])
            curr = prev[curr]
            
        return result[::-1]