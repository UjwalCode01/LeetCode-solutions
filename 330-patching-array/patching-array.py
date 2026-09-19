class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patches = 0
        miss = 1
        i = 0
        
        while miss <= n:
            # If current array element can help cover 'miss'
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            # Otherwise, greedily patch 'miss' itself
            else:
                miss += miss
                patches += 1
                
        return patches