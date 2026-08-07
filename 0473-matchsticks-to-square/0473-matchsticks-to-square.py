class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        total_len = sum(matchsticks)
        
        # Must be evenly divisible into 4 sides
        if total_len % 4 != 0:
            return False
            
        target = total_len // 4
        
        # Sort descending to try largest pieces first
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > target:
            return False
            
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                return True
                
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    
                    if backtrack(index + 1):
                        return True
                        
                    sides[i] -= matchsticks[index]
                
                # If this side length is 0, subsequent empty sides will yield identical search branches
                if sides[i] == 0:
                    break
                    
            return False
            
        return backtrack(0)
        