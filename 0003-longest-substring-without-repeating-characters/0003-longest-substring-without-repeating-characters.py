class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charMap = {}  # char -> last seen index
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in charMap and charMap[char] >= left:
                left = charMap[char] + 1

            charMap[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len