class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR n with n shifted right by 1
        n ^= (n >> 1)
        # If bits were alternating, the result will be all 1s (e.g., 3, 7, 15...)
        # A number with all 1s satisfies (n & (n + 1)) == 0
        return (n & (n + 1)) == 0