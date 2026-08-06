class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST, mapTS = {}, {}

        for charS, charT in zip(s, t):
            if (charS in mapST and mapST[charS] != charT) or \
               (charT in mapTS and mapTS[charT] != charS):
                return False

            mapST[charS] = charT
            mapTS[charT] = charS

        return True