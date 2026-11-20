import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        # LCM nikalne ke liye: (a * b) // gcd(a, b)
        lcm = math.lcm(a, b)
        
        low = min(a, b)
        high = n * min(a, b)
        
        while low < high:
            mid = (low + high) // 2
            # mid tak total magical numbers
            count = (mid // a) + (mid // b) - (mid // lcm)
            
            if count < n:
                low = mid + 1
            else:
                high = mid
                
        return low % MOD