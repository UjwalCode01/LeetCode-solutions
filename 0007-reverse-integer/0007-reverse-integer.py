class Solution(object):
    def reverse(self, x):
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            if res > (2147483647 - pop) // 10:
                return 0
                
            res = res * 10 + pop
            
        return res * sign