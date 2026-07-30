class Solution(object):

    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            # Convert 'A'-'Z' to 1-26
            value = ord(char) - ord("A") + 1
            # Base-26 positional shift
            result = result * 26 + value

        return result