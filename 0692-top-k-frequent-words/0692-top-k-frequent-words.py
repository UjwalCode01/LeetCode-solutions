from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # Count the frequency of each word
        count = Counter(words)
        
        # Sort by frequency descending (-count[word]), then lexicographically ascending (word)
        sorted_words = sorted(count.keys(), key=lambda word: (-count[word], word))
        
        # Return the top k elements
        return sorted_words[:k]