from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Ensure nums1 is the smaller array to optimize memory usage
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
            
        counts = Counter(nums1)
        res = []
        
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        return res