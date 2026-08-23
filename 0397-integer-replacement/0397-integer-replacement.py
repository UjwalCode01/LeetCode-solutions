class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        while n > 1:
            if n % 2 == 0:
                # If even, always divide by 2
                n //= 2
            elif n == 3 or (n & 3) == 1:
                # If binary ends in 01 (or n is 3), subtracting 1 yields more factors of 2
                n -= 1
            else:
                # If binary ends in 11, adding 1 yields more factors of 2 (e.g., 7 -> 8)
                n += 1
            count += 1
            
        return count