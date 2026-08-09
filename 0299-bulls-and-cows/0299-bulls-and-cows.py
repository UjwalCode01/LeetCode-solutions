from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        s_counts = Counter()
        g_counts = Counter()
        
        # First pass: count bulls and record non-matching digit frequencies
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_counts[s] += 1
                g_counts[g] += 1
                
        # Second pass: calculate cows using minimum overlapping counts
        cows = sum(min(s_counts[ch], g_counts[ch]) for ch in s_counts)
        
        return "{}A{}B".format(bulls, cows)