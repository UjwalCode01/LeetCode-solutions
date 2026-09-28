import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        
        # Sort by width ascending, and height descending if widths are equal
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract LIS on heights
        tails = []
        for _, h in envelopes:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
                
        return len(tails)