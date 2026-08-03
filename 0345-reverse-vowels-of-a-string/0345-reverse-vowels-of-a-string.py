class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to list because Python strings are immutable
        chars = list(s)
        
        # Set of vowels for O(1) lookup speed (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")
        
        left = 0
        right = len(chars) - 1

        while left < right:
            # Move left pointer forward if it's not a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            
            # Move right pointer backward if it's not a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]
            
            # Move pointers inward
            left += 1
            right -= 1

        return "".join(chars)