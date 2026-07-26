class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-indexed base-26
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            columnNumber //= 26
            
        return "".join(reversed(result))