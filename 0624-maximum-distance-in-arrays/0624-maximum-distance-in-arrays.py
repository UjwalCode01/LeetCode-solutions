class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Pehle array ki min aur max values ko initialize karo
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_dist = 0
        
        # Second array (index 1) se loop start karo
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Max distance calculate karo 
            # (Current Max - Puraana Min) aur (Puraana Max - Current Min) mein se jo bada ho
            max_dist = max(max_dist, abs(current_max - min_val), abs(max_val - current_min))
            
            # Aage ke iterations ke liye global min aur max ko update kar lo
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
            
        return max_dist