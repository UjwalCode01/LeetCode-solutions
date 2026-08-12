import bisect


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []

        for num in nums:
            # Find the insertion index for num to maintain sorted order
            idx = bisect.bisect_left(sub, num)

            # If num is larger than all elements, append it
            if idx == len(sub):
                sub.append(num)
            # Otherwise, replace the element at idx with num (greedily lower threshold)
            else:
                sub[idx] = num

        return len(sub)