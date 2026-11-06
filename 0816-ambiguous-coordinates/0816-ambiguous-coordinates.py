from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make_valid(sub: str) -> List[str]:
            res = []
            # Try placing a decimal point at every possible position
            for i in range(1, len(sub) + 1):
                left = sub[:i]
                right = sub[i:]
                
                # Check validity of left (integer) part and right (fractional) part
                # Left part cannot have leading zeros unless it is "0"
                # Right part cannot end with '0'
                if (len(left) > 1 and left[0] == '0') or (len(right) > 0 and right[-1] == '0'):
                    continue
                
                if len(right) == 0:
                    res.append(left)
                else:
                    res.append(left + "." + right)
            return res

        s = s[1:-1] # Remove outer parentheses
        n = len(s)
        ans = []

        # Split string into all possible left (X) and right (Y) parts
        for i in range(1, n):
            left_strs = make_valid(s[:i])
            right_strs = make_valid(s[i:])
            
            for x in left_strs:
                for y in right_strs:
                    ans.append(f"({x}, {y})")
                    
        return ans