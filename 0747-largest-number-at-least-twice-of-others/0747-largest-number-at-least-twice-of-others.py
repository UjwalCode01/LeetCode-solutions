class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        # Find the maximum element and its index
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        # Check against every other number in the array
        for i, val in enumerate(nums):
            if i != max_idx and max_val < 2 * val:
                return -1
                
        return max_idx