class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Keyboard rows as set structures
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        valid_words = []

        for word in words:
            # Convert word to lower case set of distinct characters
            word_set = set(word.lower())
            
            # Check if all letters belong to a single keyboard row
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                valid_words.append(word)

        return valid_words