class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_distance = 0
        n = len(nums)
        
        # Examine each bit position from 0 to 31
        for i in range(32):
            count_ones = 0
            for num in nums:
                if (num >> i) & 1:
                    count_ones += 1
            
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
            
        return total_distance