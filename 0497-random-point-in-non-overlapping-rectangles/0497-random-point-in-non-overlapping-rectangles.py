import bisect
import random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.prefix_sums = []
        total_points = 0
        
        for x1, y1, x2, y2 in rects:
            # Number of integer points in the current rectangle
            pts = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_points += pts
            self.prefix_sums.append(total_points)

    def pick(self):
        """
        :rtype: List[int]
        """
        # Pick a random point index in [1, total_points]
        target = random.randint(1, self.prefix_sums[-1])
        
        # Binary search to find which rectangle contains this target index
        idx = bisect.bisect_left(self.prefix_sums, target)
        
        x1, y1, x2, y2 = self.rects[idx]
        
        # Pick a uniform random point within the selected rectangle bounds
        return [random.randint(x1, x2), random.randint(y1, y2)]