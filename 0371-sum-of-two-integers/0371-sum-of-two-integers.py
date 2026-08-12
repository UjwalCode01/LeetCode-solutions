class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32-bit mask to simulate 32-bit integer overflow
        mask = 0xFFFFFFFF
        # Mask to check if the result is negative in 32-bit signed representation
        max_int = 0x7FFFFFFF

        while b != 0:
            # XOR calculates the sum without carry
            # AND calculates the carry, then shift left by 1
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # If 'a' exceeds max positive 32-bit signed integer, convert to negative
        return a if a <= max_int else ~(a ^ mask)