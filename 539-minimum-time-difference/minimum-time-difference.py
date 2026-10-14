class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # Convert all "HH:MM" strings to total minutes
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(':'))
            minutes.append(h * 60 + m)
            
        # Sort the minutes
        minutes.sort()
        
        # Initialize the minimum difference with the wrap-around difference across midnight
        min_diff = (24 * 60 - minutes[-1]) + minutes[0]
        
        # Check differences between consecutive adjacent elements
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            if diff < min_diff:
                min_diff = diff
                
        return min_diff