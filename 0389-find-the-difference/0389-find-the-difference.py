class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        
        # XOR all characters in s and t
        for char in s:
            res ^= ord(char)
        for char in t:
            res ^= ord(char)
            
        # Convert ASCII value back to character
        return chr(res)