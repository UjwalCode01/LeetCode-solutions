class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        # Sort dictionary: primary key = length descending (-len), secondary key = alphabetical
        dictionary.sort(key=lambda word: (-len(word), word))
        
        for word in dictionary:
            # Check if 'word' is a subsequence of 's' using two pointers
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
            
            if i == len(word):
                return word
                
        return ""