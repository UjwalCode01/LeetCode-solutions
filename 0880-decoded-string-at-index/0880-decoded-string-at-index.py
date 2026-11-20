class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        
        # Step 1: Total decoded length nikalna
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
                
        # Step 2: Reverse mein k-th (1-indexed) character dhoondhna
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            k %= size
            
            if k == 0 and ch.isalpha():
                return ch
                
            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1
                
        return ""