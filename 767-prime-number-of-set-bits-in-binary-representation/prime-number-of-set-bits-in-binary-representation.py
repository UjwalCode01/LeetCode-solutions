class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Set of prime numbers up to 20 (since 2^20 exceeds constraints, max set bits is around 20)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        for x in range(left, right + 1):
            if bin(x).count('1') in primes:
                count += 1
                
        return count