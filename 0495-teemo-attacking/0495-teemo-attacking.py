class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        
        total_time = 0
        
        for i in range(len(timeSeries) - 1):
            # Add whichever is smaller: full duration or the gap between current and next attack
            total_time += min(duration, timeSeries[i + 1] - timeSeries[i])
            
        # Add full duration for the last attack
        return total_time + duration