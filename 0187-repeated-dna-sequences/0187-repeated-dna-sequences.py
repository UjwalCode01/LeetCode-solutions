class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            window = s[i:i+10]
            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)
                
        return list(repeated)