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

        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for money in houses:
                temp = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = temp
            return prev1

        # Compare robbing excluding the last house vs excluding the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))