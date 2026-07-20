import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Numbers ki list banayein: [1, 2, 3, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # 0-based indexing ke liye k ko 1 kam kar dete hain
        k -= 1
        
        ans = ""
        
        # Loop chalayenge jab tak saare numbers use nahi ho jaate
        while n > 0:
            # Ek block ka size nikalte hain: (n-1)!
            factorial = math.factorial(n - 1)
            
            # Pata lagate hain ki kaunsa number select hoga
            index = k // factorial
            
            # Us number ko ans mein jodte hain aur list se hata dete hain
            ans += numbers.pop(index)
            
            # Agle round ke liye k ko update karte hain aur n ko kam karte hain
            k %= factorial
            n -= 1
            
        return ans