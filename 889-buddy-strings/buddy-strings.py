class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Case 1: Lengths must be equal
        if len(s) != len(goal):
            return False
        
        # Case 2: If strings are identical, we need at least one duplicate character to swap
        if s == goal:
            return len(set(s)) < len(s)
        
        # Case 3: Find indices where characters differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                
        # We must have exactly 2 mismatches, and swapping them must make them match
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]