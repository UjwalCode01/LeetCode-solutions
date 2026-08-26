class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        length = len(binary)
        
        # f[i] stores count of binary numbers of length i without consecutive ones
        f = [0] * (length + 1)
        f[0] = 1
        f[1] = 2
        for i in range(2, length + 1):
            f[i] = f[i - 1] + f[i - 2]
            
        ans = 0
        prev_bit = 0
        
        for i in range(length):
            if binary[i] == '1':
                ans += f[length - i - 1]
                
                if prev_bit == 1:
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0
                
        return ans + 1