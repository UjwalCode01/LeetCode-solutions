class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with element at low
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in the right place, just move forward
                mid += 1
            else:  # nums[mid] == 2
                # Swap current element with element at high
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                # Note: We do NOT increment mid here because the swapped 
                # value from high still needs to be processed.