import heapq

class Solution(object):
    def getSkyline(self, buildings):
        # 1. Collect all critical points / events
        events = []
        for l, r, h in buildings:
            # Start event: negative height (helps sort highest height first if x is same)
            events.append((l, -h, r))
            # End event: height 0 (signals point of exit)
            events.append((r, 0, 0))
            
        # 2. Sort events by x coordinate first, then by height
        events.sort()
        
        # res = [[x, height]], start with ground
        res = [[0, 0]]
        # max_heap = [(-height, right_end)]
        hp = [(0, float('inf'))]
        
        for x, neg_h, r in events:
            # If it's a start event, push to heap
            if neg_h < 0:
                heapq.heappush(hp, (neg_h, r))
                
            # Pop all buildings from heap that ended at or before current x
            while hp[0][1] <= x:
                heapq.heappop(hp)
                
            # Current maximum active height
            curr_max = -hp[0][0]
            
            # If height changed from last added point, add new keypoint
            if res[-1][1] != curr_max:
                res.append([x, curr_max])
                
        return res[1:]