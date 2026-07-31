class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero element into the next available slot
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1