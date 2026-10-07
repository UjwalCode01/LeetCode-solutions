import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Cannot measure more water than total combined capacity
        if target > x + y:
            return False
        
        # Target must be a multiple of gcd(x, y)
        return target % math.gcd(x, y) == 0