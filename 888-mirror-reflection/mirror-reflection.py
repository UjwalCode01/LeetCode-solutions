import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Divide both p and q by their GCD to find the smallest scaling factor
        g = math.gcd(p, q)
        p //= g
        q //= g
        
        # p is even means it hits the left wall (not a corner receptor except 0 indirectly)
        # p is odd means it hits the right wall
        # q is even means the vertical count is even (receptor 0)
        # q is odd means the vertical count is odd (receptor 1 or 2)
        
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1