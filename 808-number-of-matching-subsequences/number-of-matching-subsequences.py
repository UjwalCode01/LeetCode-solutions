from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Group words by the character they are currently waiting for
        waiting = defaultdict(list)
        
        for word in words:
            waiting[word[0]].append((word, 0))
            
        matching_count = 0
        
        # Iterate through each character in s
        for char in s:
            current_bucket = waiting[char]
            waiting[char] = []
            
            for word, idx in current_bucket:
                idx += 1
                if idx == len(word):
                    matching_count += 1
                else:
                    waiting[word[idx]].append((word, idx))
                    
        return matching_count