class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0

        ans = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                current = 1

            ans = max(ans, current)

        return ans