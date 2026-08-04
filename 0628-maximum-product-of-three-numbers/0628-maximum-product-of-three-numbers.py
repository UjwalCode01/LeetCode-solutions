class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        # Case 1: Product of 3 largest numbers
        # Case 2: Product of 2 smallest (negative) numbers and the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])