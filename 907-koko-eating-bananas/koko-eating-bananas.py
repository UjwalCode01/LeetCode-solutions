import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            # Total hours needed at eating speed `mid`
            hours_needed = sum(math.ceil(pile / mid) for pile in piles)

            if hours_needed <= h:
                # Koko can finish in time; try a slower (smaller) speed
                right = mid
            else:
                # Too slow; need a faster (larger) speed
                left = mid + 1

        return left