class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define the set of characters for each row on the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            # Convert word to lower-case set of characters for comparison
            word_set = set(word.lower())
            
            # Check if all characters in the word belong to a single row
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                result.append(word)
                
        return result