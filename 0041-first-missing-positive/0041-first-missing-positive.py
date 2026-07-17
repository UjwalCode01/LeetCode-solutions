class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # 1. Cyclic Sort: Place each number in its correct slot if possible
        for i in range(n):
            # Keep swapping until the current element is in its correct position,
            # or it falls out of the valid range [1, n], or it is a duplicate.
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Target index where nums[i] belongs
                correct_idx = nums[i] - 1
                # Swap nums[i] with the element at its correct position
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # 2. Find the first index where the number doesn't match the slot
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 3. If all slots are filled correctly [1, 2, ..., n], the missing one is n + 1
        return n + 1