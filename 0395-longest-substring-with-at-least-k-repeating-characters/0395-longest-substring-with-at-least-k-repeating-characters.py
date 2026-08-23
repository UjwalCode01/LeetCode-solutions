class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Base case: string shorter than k cannot have any valid substring
        if len(s) < k:
            return 0

        # Count frequencies of each character in current string
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Find a character with frequency < k to split on
        for char, freq in count.items():
            if freq < k:
                # Split string by the invalid character and recurse on all parts
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))

        # If every character appears at least k times, the entire string is valid
        return len(s)