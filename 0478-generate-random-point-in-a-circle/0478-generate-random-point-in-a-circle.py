import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # Take the square root of a random uniform value to ensure uniform area distribution
        r = self.radius * math.sqrt(random.random())
        # Generate a random angle from 0 to 2*pi
        theta = random.random() * 2 * math.pi
        
        # Convert polar coordinates to Cartesian coordinates and offset by center
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        
        return [x, y]