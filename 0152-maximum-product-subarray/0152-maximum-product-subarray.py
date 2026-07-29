class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curr_max, curr_min = 1, 1

        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue

            # Store temporary max before updating
            tmp = curr_max * n
            curr_max = max(tmp, curr_min * n, n)
            curr_min = min(tmp, curr_min * n, n)

            res = max(res, curr_max)

        return res