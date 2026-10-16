class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                # Recursively process the inner part, wrap with '1' and '0'
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
                
        # Sort in descending order to get the lexicographically largest result
        res.sort(reverse=True)
        return "".join(res)
        