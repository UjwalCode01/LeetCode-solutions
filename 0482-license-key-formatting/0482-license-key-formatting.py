class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Remove dashes and convert everything to uppercase
        s = s.replace("-", "").upper()
        
        res = []
        count = 0
        
        # Traverse the cleaned string from right to left
        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            count += 1
            # After every k characters (and if we aren't at the very end), add a dash
            if count == k and i != 0:
                res.append("-")
                count = 0
                
        # Since we traversed backwards, reverse the result list and join into a string
        return "".join(res[::-1])