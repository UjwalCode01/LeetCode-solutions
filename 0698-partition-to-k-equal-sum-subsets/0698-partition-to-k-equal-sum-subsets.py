class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """:type nums: List[int] :type k: int :rtype: bool"""
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False
            
        memo = {}
        
        def backtrack(mask, current_sum):
            if mask == (1 << len(nums)) - 1:
                return True
            if mask in memo:
                return memo[mask]
                
            for i in range(len(nums)):
                if (mask & (1 << i)) == 0:
                    if current_sum + nums[i] <= target:
                        if backtrack(mask | (1 << i), (current_sum + nums[i]) % target):
                            memo[mask] = True
                            return True
                    elif current_sum == 0:
                        break
                        
            memo[mask] = False
            return False
            
        return backtrack(0, 0)