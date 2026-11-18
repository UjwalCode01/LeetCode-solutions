class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Generate digit frequency signature for n
        from collections import Counter
        n_count = Counter(str(n))
        
        # Check against all powers of 2 up to 10^9 (since n <= 10^9)[cite: 3]
        for i in range(30):
            if Counter(str(1 << i)) == n_count:
                return True
                
        return False