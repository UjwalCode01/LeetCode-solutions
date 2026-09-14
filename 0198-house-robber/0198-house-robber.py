class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0

        # rob1: max money robbed up to house i-2
        # rob2: max money robbed up to house i-1
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2