class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = sentence.split()
        res = []
        
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            
            # Add 'a' corresponding to the 1-based word index
            new_word += "a" * i
            res.append(new_word)
            
        return " لج ".join(res).replace(" لج ", " ") # standard join is faster: " ".join(res)