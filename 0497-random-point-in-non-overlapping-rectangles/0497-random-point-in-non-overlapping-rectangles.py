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
        
        for a, b, x, y in rects:
            # Number of integer points in the rectangle = (width + 1) * (height + 1)
            points = (x - a + 1) * (y - b + 1)
            total_points += points
            self.prefix_sums.append(total_points)
            
        self.total_points = total_points

    def pick(self):
        """
        :rtype: List[int]
        """
        # Pick a random point index from 1 to total_points
        choice = random.randint(1, self.total_points)
        
        # Find which rectangle this point falls into using binary search
        rect_index = bisect.bisect_left(self.prefix_sums, choice)
        
        # Retrieve the chosen rectangle coordinates
        a, b, x, y = self.rects[rect_index]
        
        # Pick a random x and y coordinate within the rectangle
        rx = random.randint(a, x)
        ry = random.randint(b, y)
        
        return [rx, ry]