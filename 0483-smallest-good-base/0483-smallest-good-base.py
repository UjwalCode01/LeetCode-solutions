import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)
        # Maximum length of 1's in base 2
        max_m = int(math.log2(N)) + 1
        
        # Iterate over possible number of digits (m) from largest to smallest
        for m in range(max_m, 2, -1):
            # Estimate base k using integer root
            k = int(N ** (1 / (m - 1)))
            
            if k >= 2:
                # Sum of geometric series: 1 + k + k^2 + ... + k^(m-1)
                total = (pow(k, m) - 1) // (k - 1)
                if total == N:
                    return str(k)
        
        # Fallback for m = 2, where k = N - 1
        return str(N - 1)