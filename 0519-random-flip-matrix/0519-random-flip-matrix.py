import random

class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.V = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        # Pick a random index in the current available pool
        r = random.randint(0, self.total - 1)
        self.total -= 1
        
        # Determine actual value mapped at position r
        idx = self.V.get(r, r)
        
        # Map r to the element at the current end of the pool (self.total)
        self.V[r] = self.V.get(self.total, self.total)
        
        # Convert 1D index to 2D matrix coordinates
        return [idx // self.n, idx % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.V.clear()
        self.total = self.m * self.n