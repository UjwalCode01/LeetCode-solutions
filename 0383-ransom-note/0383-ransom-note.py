from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count frequency of each character in magazine and ransomNote
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)

        # Ensure magazine has enough of each letter needed for ransomNote
        for char, count in ransom_counts.items():
            if magazine_counts[char] < count:
                return False

        return True