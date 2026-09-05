class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: XOR all elements to get xor_all = a ^ b
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        # Step 2: Find a rightmost set bit (differing bit between a and b)
        diff_bit = xor_all & (-xor_all)
        
        # Step 3: Divide numbers into two groups and XOR separately
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]