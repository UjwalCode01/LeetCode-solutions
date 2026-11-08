class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        # Collect numbers that appear on both sides of the same card
        same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        
        ans = 999999  # Initialize with a large value
        
        # Check all numbers in fronts and backs
        for x in fronts + backs:
            if x not in same:
                if x < ans:
                    ans = x
                    
        return ans if ans != 999999 else 0