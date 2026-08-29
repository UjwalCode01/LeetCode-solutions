class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Create a mask with all 1s of the same length as num's binary representation
        mask = (1 << num.bit_length()) - 1
        
        # XOR with the mask to flip all bits
        return num ^ mask