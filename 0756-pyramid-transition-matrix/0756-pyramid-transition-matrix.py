from collections import defaultdict
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Preprocess allowed patterns: (left, right) -> list of top blocks
        allowed_map = defaultdict(list)
        for pattern in allowed:
            allowed_map[(pattern[0], pattern[1])].append(pattern[2])
            
        @lru_cache(None)
        def can_reach_top(row: str) -> bool:
            # Base case: agar row me sirf 1 block bacha hai, matlab top par pahunch gaye
            if len(row) == 1:
                return True
            
            # Helper function to generate all possible next rows
            def get_next_rows(idx: int, current_next_row: str) -> list[str]:
                if idx == len(row) - 1:
                    return [current_next_row]
                
                left = row[idx]
                right = row[idx + 1]
                key = (left, right)
                
                if key not in allowed_map:
                    return []
                
                results = []
                for top in allowed_map[key]:
                    results.extend(get_next_rows(idx + 1, current_next_row + top))
                return results
            
            next_rows = get_next_rows(0, "")
            
            # Agar koi bhi valid next row top tak le jaye toh True return karo
            for next_row in next_rows:
                if can_reach_top(next_row):
                    return True
                    
            return False

        return can_reach_top(bottom)