class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0

        for num in nums:
            # Update 'ones' with bits that appeared once
            ones = (ones ^ num) & ~twos
            # Update 'twos' with bits that appeared twice
            twos = (twos ^ num) & ~ones

        return ones