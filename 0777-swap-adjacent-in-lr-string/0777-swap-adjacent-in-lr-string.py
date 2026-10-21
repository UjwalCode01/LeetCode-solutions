class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False
        
        n = len(start)
        i = 0  # pointer for start
        j = 0  # pointer for result
        
        while i < n or j < n:
            # Skip 'X' characters in start
            while i < n and start[i] == 'X':
                i += 1
            # Skip 'X' characters in result
            while j < n and result[j] == 'X':
                j += 1
                
            # If one reaches the end before the other
            if i == n or j == n:
                return i == n and j == n
            
            # Characters must match
            if start[i] != result[j]:
                return False
            
            # Check movement rules
            if start[i] == 'L' and i < j:  # L cannot move right
                return False
            if start[i] == 'R' and i > j:  # R cannot move left
                return False
                
            i += 1
            j += 1
            
        return True