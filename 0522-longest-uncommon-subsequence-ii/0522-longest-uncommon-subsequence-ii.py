class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # Helper function to check if s1 is a subsequence of s2
        def isSubsequence(s1, s2):
            i = 0
            for char in s2:
                if i < len(s1) and s1[i] == char:
                    i += 1
            return i == len(s1)

        # Sort strings by length in descending order
        strs.sort(key=len, reverse=True)

        for i, s1 in enumerate(strs):
            is_uncommon = True
            for j, s2 in enumerate(strs):
                if i == j:
                    continue
                # If s1 is a subsequence of s2, it's not uncommon
                if isSubsequence(s1, s2):
                    is_uncommon = False
                    break
            
            # Since we sorted by length, the first uncommon string found has the maximum length
            if is_uncommon:
                return len(s1)

        return -1