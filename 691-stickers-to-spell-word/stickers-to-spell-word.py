class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        n = len(target)
        # Precompute character counts for each sticker
        sticker_counts = []
        for sticker in stickers:
            count = [0] * 26
            for char in sticker:
                count[ord(char) - ord('a')] += 1
            sticker_counts.append(count)
            
        memo = {}
        
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
            if mask in memo:
                return memo[mask]
            
            res = float('inf')
            
            # Find the first uncovered character to reduce unnecessary branching
            first_uncovered = 0
            while first_uncovered < n and (mask & (1 << first_uncovered)):
                first_uncovered += 1
                
            target_char = target[first_uncovered]
            
            # Try every sticker that contains the uncovered character
            for s_count in sticker_counts:
                if s_count[ord(target_char) - ord('a')] == 0:
                    continue
                    
                next_mask = mask
                curr_s_count = list(s_count)
                
                for i in range(n):
                    if not (next_mask & (1 << i)):
                        char_idx = ord(target[i]) - ord('a')
                        if curr_s_count[char_idx] > 0:
                            curr_s_count[char_idx] -= 1
                            next_mask |= (1 << i)
                            
                if next_mask != mask:
                    res = min(res, 1 + dp(next_mask))
                    
            memo[mask] = res
            return res

        ans = dp(0)
        return ans if ans != float('inf') else -1