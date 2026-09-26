class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        total_slices = 0
        current_streak = 0
        
        for i in range(2, n):
            # Check if the difference between consecutive elements is the same
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_streak += 1
                total_slices += current_streak
            else:
                current_streak = 0
                
        return total_slices