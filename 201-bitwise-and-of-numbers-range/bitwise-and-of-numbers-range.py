class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shifts = 0
        # Right shift until both numbers are equal (finding common prefix)
        while left < right:
            left >>= 1
            right >>= 1
            shifts += 1
            
        # Left shift to append trailing zeros back
        return left << shifts