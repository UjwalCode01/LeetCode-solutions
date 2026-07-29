class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= (n - 1)  # Clears the lowest set bit
            count += 1
        return count