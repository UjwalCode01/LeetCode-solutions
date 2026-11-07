class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Use a set to remove duplicate words
        good = set(words)
        
        # Remove any word that is a suffix of another word in the set
        for word in words:
            for i in range(1, len(word)):
                good.discard(word[i:])
                
        # The length is the sum of lengths of all remaining words plus 1 for each '#'
        return sum(len(word) + 1 for word in good)