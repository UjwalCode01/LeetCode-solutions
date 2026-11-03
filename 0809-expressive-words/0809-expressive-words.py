class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def check(word: str) -> bool:
            i, j = 0, 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] != word[j]:
                    return False
                
                # s mein character group ki length count karo
                i2 = i
                while i2 < n and s[i2] == s[i]:
                    i2 += 1
                len1 = i2 - i
                
                # word mein character group ki length count karo
                j2 = j
                while j2 < m and word[j2] == word[j]:
                    j2 += 1
                len2 = j2 - j
                
                # Validations check karo
                if len2 > len1:
                    return False
                if len2 < len1 and len1 < 3:
                    return False
                
                i, j = i2, j2
            
            return i == n and j == m

        return sum(check(w) for w in words)