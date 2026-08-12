from collections import Counter


class Solution(object):

    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # Store frequencies of all possible sums of pairs from nums1 and nums2
        sum_counts = Counter(a + b for a in nums1 for b in nums2)

        count = 0
        # For each pair sum in nums3 and nums4, find its complement -(c + d)
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += sum_counts[target]

        return count