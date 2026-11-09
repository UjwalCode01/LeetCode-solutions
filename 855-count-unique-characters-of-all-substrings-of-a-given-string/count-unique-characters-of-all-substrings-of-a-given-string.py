from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Map each character to a list of its indices in the string
        index_map = defaultdict(list)
        for i, char in enumerate(s):
            index_map[char].append(i)
            
        total_sum = 0
        n = len(s)
        
        # Calculate contribution for each character group
        for indices in index_map.values():
            for k in range(len(indices)):
                prev_idx = indices[k - 1] if k > 0 else -1
                curr_idx = indices[k]
                next_idx = indices[k + 1] if k + 1 < len(indices) else n
                
                # Contribution = (choices for left boundary) * (choices for right boundary)
                total_sum += (curr_idx - prev_idx) * (next_idx - curr_idx)
                
        return total_sum