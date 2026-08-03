from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count frequency of each character in the string
        counts = Counter(s)
        
        # Find the first character with a count of 1 and return its index
        for index, char in enumerate(s):
            if counts[char] == 1:
                return index
                
        return -1