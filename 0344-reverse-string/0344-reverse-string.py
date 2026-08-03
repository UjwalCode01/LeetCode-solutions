class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Swap characters at left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Move pointers toward the center
            left += 1
            right -= 1