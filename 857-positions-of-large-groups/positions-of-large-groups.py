class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        n = len(s)
        i = 0
        
        while i < n:
            j = i
            # Find the end of the current group of identical characters
            while j < n and s[j] == s[i]:
                j += 1
            
            # Check if the group has 3 or more characters
            if j - i >= 3:
                res.append([i, j - 1])
                
            # Move to the next new character group
            i = j
            
        return res