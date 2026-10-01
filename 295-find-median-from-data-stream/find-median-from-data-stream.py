import heapq

class MedianFinder(object):

    def __init__(self):
        # max-heap for the smaller half (invert numbers to simulate max-heap in Python)
        self.small = []
        # min-heap for the larger half
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Always insert into max-heap (small) first
        heapq.heappush(self.small, -num)
        
        # Ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes (small can have at most 1 more element than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0