class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        mask = 0
        
        # Iterate from Most Significant Bit (MSB) to Least Significant Bit (LSB)
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            
            # Target candidate with the i-th bit set to 1
            candidate = max_xor | (1 << i)
            
            # Check if two prefixes exist that XOR to candidate
            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    max_xor = candidate
                    break
                    
        return max_xor