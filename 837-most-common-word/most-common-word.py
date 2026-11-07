import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Convert paragraph to lowercase and extract words using regex (ignoring punctuation)
        words = re.findall(r'\w+', paragraph.lower())
        
        # Convert banned list to a set for O(1) lookups
        banned_set = set(banned)
        
        # Filter out banned words and count frequencies
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Return the most common word
        return word_counts.most_common(1)[0][0]