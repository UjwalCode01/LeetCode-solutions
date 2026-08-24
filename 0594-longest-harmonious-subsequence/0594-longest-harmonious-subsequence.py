from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_len = 0
        
        for num in counts:
            if num + 1 in counts:
                max_len = max(max_len, counts[num] + counts[num + 1])
                
        return max_len