class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        num = int(n)
        
        # Base edge cases for boundary shifts
        candidates = {
            10**(length - 1) - 1,  # e.g., 999 for length 4
            10**length + 1          # e.g., 10001 for length 4
        }
        
        # Extract the prefix (first half, including middle digit for odd lengths)
        prefix = int(n[:(length + 1) // 2])
        
        # Try prefix, prefix - 1, and prefix + 1
        for p in (prefix - 1, prefix, prefix + 1):
            p_str = str(p)
            # If length is odd, drop the last char before mirroring
            if length % 2 == 0:
                cand = p_str + p_str[::-1]
            else:
                cand = p_str + p_str[:-1][::-1]
            candidates.add(int(cand))
        
        # Remove original number as a valid candidate
        candidates.discard(num)
        
        # Find candidate with minimal absolute difference (break ties with smaller value)
        return str(min(candidates, key=lambda x: (abs(x - num), x)))