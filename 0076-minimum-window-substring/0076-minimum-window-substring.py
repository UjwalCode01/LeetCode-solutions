from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""

        # Frequency map for characters in t
        count_t = Counter(t)
        window = {}

        # have: number of unique characters in current window that meet t's frequency requirement
        # need: total unique characters required from t
        have, need = 0, len(count_t)
        
        res = [-1, -1]
        res_len = float("inf")
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # If character frequency requirement is satisfied
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Try to shrink window from the left while it remains valid
            while have == need:
                # Update smallest window result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Pop from left to shrink
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""