class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
        for num in nums:
            idx = bisect.bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)