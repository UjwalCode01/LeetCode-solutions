class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split() without arguments automatically splits by multiple whitespaces 
        # and trims leading/trailing spaces.
        words = s.split()
        
        # Reverse the list of words and join them with a single space
        return ' '.join(words[::-1])